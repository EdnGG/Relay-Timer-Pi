import RPi.GPIO as GPIO
import time
import datetime
from time import sleep

GPIO.setmode(GPIO.BCM)

slleptime = .1

#GPIO pin on the component
lightPin = 17
buttonPin = 27

GPIO.setup(lightPin, GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.output(lightPin, False)

try: 
    while True:
        GPIO.output(lightPin, not GPIO.input(buttonPin))
        sleep(.1)
finally:
    GPIO.output(lightPin, False)
    GPIO.cleanup()
