# import GPIO and time
import RPi.GPIO as GPIO
import time
import datetime

#  LED and Switch Button 
LedPin = 17
ButtonPin = 27

# set GPIO numbering mode and define output pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

#LED and Switch seccion
GPIO.setup(LedPin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(ButtonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)


# cycle those relays

# adding 1 on each cicle
counterCicles = 0   
counter = 0
counter1 = 0
counter2 = 0

# Getting date
today = datetime.datetime.now()
formatDate = today.strftime("%A, %B, %d, %Y")


# Getting name
name = input("Technichian name: ")

# Getting actuators serial numbers
actuatorRelay1 = input("Please provide Act serial number for relay #1" + '\n')
actuatorRelay2 = input("Please provide Act serial number for relay #2" + '\n')
actuatorRelay3 = input("Please provide Act serial number for relay #3" + '\n')


print('\n' + "Welcome ",  name + '\n'+ '\n' + "Today is: " + str(formatDate) + '\n' + '\n')

# def start():

try:
    while counterCicles <= 5:
        GPIO.output(21, True)     
        counter = counter + 1
        counterCicles = counterCicles + 1
        print("Actuator number: "+ str(actuatorRelay1)+" On relay 1. Cicle #:" + str(counter) + '\n')
        if GPIO.input(ButtonPin) == 0:
            print("Actuator reach the desire distance")
        else:
            print("Actuator dont reach the desire distance")
        time.sleep(4)
        GPIO.output(21, False)
        GPIO.output(20, True)
        counter1 = counter1 + 1
        print("Actuator number: "+ str(actuatorRelay2)+" On relay 2. Cicle #:" + str(counter) + '\n')
        if GPIO.input(ButtonPin) == 0:
            print("Actuator reach the desire distance")
        else:
            print("Actuator dont reach the desire distance")
        time.sleep(4)            
        GPIO.output(20, False)
        GPIO.output(26, True)
        counter2 = counter2 + 1
        print("Actuator number: "+ str(actuatorRelay3)+" On relay 3. Cicle #:" + str(counter) + '\n')
        if GPIO.input(ButtonPin) == 0:
            print("Actuator reach the desire distance")
        else:
            print("Actuator dont reach the desire distance")
        time.sleep(4)
        GPIO.output(26, False)
        time.sleep(4)


finally:


        # cleanup the GPIO before finishing :)
    print("Actuator number "+str(actuatorRelay1)+" On relay #1 runs: " + str(counter) + " Cicles")
    print("Actuator number "+str(actuatorRelay2)+" On relay #2 runs: " + str(counter1) + " Cicles")
    print("Actuator number "+str(actuatorRelay3)+" On relay #3 runs: " + str(counter2) + " Cicles")
    GPIO.cleanup()


