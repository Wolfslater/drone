from os import system
from djitellopy import tello
from time import sleep
import cv2
from keyboard import is_pressed

def connectTello(tellonum):
    ssid = "TELLO-" + tellonum
    return system(f'''cmd /c "netsh wlan connect name={ssid}"''')

def isPressed(speed):
    control = [0, 0, 0, 0]

    if is_pressed("a"): control[0] = -speed
    elif is_pressed("d"): control[0] = speed
    if is_pressed("s"): control[1] = -speed
    elif is_pressed("w"): control[1] = speed
    if is_pressed("k"): control[2] = -speed
    elif is_pressed("i"): control[2] = speed
    if is_pressed("j"): control[3] = -speed
    elif is_pressed("l"): control[3] = speed
    return control

def draw_speed(img, x, y, speed):
    cv2.rectangle(img, (x, y), (x + 30, y + 100), (255, 255, 0), 3)
    cv2.rectangle(img, (x, y + 100 - speed), (x + 30, y + 100), (25, 255, 0), cv2.FILLED)

def show_img(speed):
    img = drone.get_frame_read().frame
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    cv2.putText(img, f"{drone.get_distance_tof()}CM", (50, 100), cv2.QT_FONT_NORMAL, 1, (70, 240, 255), 2)
    cv2.putText(img, f"Battery life: {drone.get_battery()}%", (690, 100), cv2.QT_FONT_NORMAL, 1, (50, 240, 255), 2)
    draw_speed(img, 10, 10, speed)
    return img

drone = tello.Tello()