from drone_functions import *

if __name__ == '__main__':
    on_of = False
    connectTello("F09956")
    drone.connect()
    if on_of:
        drone.streamon()
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    speed = 50
    control = [0, 0, 0, 0]
    i = 0

    while not is_pressed("esc"):
        if is_pressed("z") and not drone.is_flying: drone.takeoff()
        if is_pressed("x") and drone.is_flying: drone.land()
        if is_pressed("e"): drone.set_video_direction(drone.CAMERA_DOWNWARD)
        if is_pressed("q"): drone.set_video_direction(drone.CAMERA_FORWARD)
        if is_pressed("+")and speed < 100:
            sleep(0.01)
            speed = max(100, speed +1)
        if is_pressed("-") and speed > 0:
            sleep(0.01)
            speed = min(0, speed - 1)

        control = isPressed(speed)
        drone.send_rc_control(control[0], control[1], control[2], control[3])
        if on_of:
            img = show_img(speed)

        if is_pressed("space"):
            cv2.imwrite(f"file{i}.jpg", img)
            sleep(0.1)
            i += 1

        cv2.imshow("Output", img)
        cv2.waitKey(1)
