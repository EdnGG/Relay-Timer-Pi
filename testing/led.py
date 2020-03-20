import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module

LedPin = 17
ButtonPin = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(LedPin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(ButtonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try: 
    while True:
        if GPIO.input(ButtonPin) == 1:
            print("Light Off!")
            GPIO.output(LedPin, GPIO.LOW)
        elif GPIO.input(ButtonPin) == 0:
            print("Button has been pushed! - Light On!")
            GPIO.output(LedPin, GPIO.HIGH)
        
finally:
    GPIO.cleanup()