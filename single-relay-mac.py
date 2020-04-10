# import GPIO and time
import RPi.GPIO as GPIO
import time
import datetime

#  LED and Switch Button
LedPin = 17
ButtonPin = 27

# set GPIO numbering mode and define output pins
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

# LED and Switch seccion
GPIO.setup(LedPin, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(ButtonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)


# cycle those relays

# adding 1 on each cicle
counterCicles = 0
counter = 0
timesActuatorReachDistance = 0

# Getting date
today = datetime.datetime.now()
formatDate = today.strftime("%A, %B, %d, %Y")


# Getting name, email
name = input("Technichian name: ")
email = input(
    "Please provide an e-mail where you woulld like to get the test report")

# Getting actuators serial numbers
actuatorRelay1 = input("Provide the Actuator #  place on relay #1" + '\n')

print('\n' + "Welcome ",  name + '\n' + '\n' +
      "Today is: " + str(formatDate) + '\n' + '\n')

try:
    while counterCicles <= 5:
        GPIO.output(21, True)
        counter = counter + 1
        counterCicles = counterCicles + 1
        print("Actuator number: " + str(actuatorRelay1) +
              " On relay 1. Cicle #:" + str(counter) + '\n')
        time.sleep(40)
        if GPIO.input(ButtonPin) == 0:
            timesActuatorReachDistance = timesActuatorReachDistance + 1
            print("Actuator reach the desire distance" + "\n")
            print("Times actuator reached desire distance: " +
                  str(timesActuatorReachDistance))
        else:
            print("Actuator dont reach the desire distance")
        time.sleep(10)
        print('getting ready for next cicle')
        GPIO.output(21, False)
        time.sleep(5)


finally:
    # cleanup the GPIO before finishing :)
    print("Actuator number "+str(actuatorRelay1) +
          " On relay #1 runs: " + str(counter) + " Cicles")
    GPIO.cleanup()
