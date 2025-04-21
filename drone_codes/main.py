from drone_functions import *

if __name__ == '__main__':
    connectTello("F09947")
    drone.connect()
    speed = 50
    i = 0

    while not is_pressed("esc"):
        control = [0, 0, 0, 0]
        print(control)
        drone.streamon()
        if is_pressed("z") and not drone.is_flying: drone.takeoff()
        elif is_pressed("x") and drone.is_flying: drone.land()
        camera()

        if is_pressed("+")and speed < 100:
            sleep(0.001)
            speed += 1
        elif is_pressed("-") and speed > 0:
            sleep(0.001)
            speed -= 1
        isPressed(speed)
            
        drone.send_rc_control(control[0], control[1], control[2], control[3])
        img = show_img(speed)
        if is_pressed("space"):
            cv2.imwrite(f"file{i}.jpg", img)
            i += 1
            sleep(0.5)

        cv2.imshow("Output", img)
        cv2.waitKey(1)
