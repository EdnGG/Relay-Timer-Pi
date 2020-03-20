from time import sleep
from gpiozero import Button
button = Button(2)
cicle = 0


def pressButton():
    while True:
        # button.wait_for_press()
        button.when_pressed()
        print('button has been pressed')
        button.when_released()
        print('cicle number:' + str(cicle + 1))
        sleep(5)


pressButton()
