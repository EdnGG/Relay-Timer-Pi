# import GPIO and time
import RPi.GPIO as GPIO
import time
import datetime


# set GPIO numbering mode and define output pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

# cycle those relays

# adding 1 on each cicle
cicles = 0   
counter = 0
counter1 = 0
counter2 = 0

# Getting date

today = datetime.datetime.now()
formatDate = today.strftime("%A, %B, %d, %Y")

# Getting serial numbers for actutors tested

actuatorRelay1 = 1711303567
actuatorRelay2 = 1711303000
actuatorRelay3 = 1711306777

# Getting name

name = input("Whats your name bruhh!")

print("Welcome ",  name +'\n'+"Today is: " + str(formatDate) + '\n' + '\n')

for i in range(0,10):
    GPIO.output(21, True)
    counter = counter + 1
    cicles = cicles + 1
    # print("Actuator on relay 1. Cicle #:" + str(counter) + '\n')
    print("Actuator number: "+ str(actuatorRelay1)+" On relay 1. Cicle #:" + str(counter) + '\n')
    time.sleep(3)
    GPIO.output(21, False)
    time.sleep(3)

# try:
#     while cicles <= 10:
#         GPIO.output(21, True)
#         counter = counter + 1
#         cicles = cicles + 1
#         # print("Actuator on relay 1. Cicle #:" + str(counter) + '\n')
#         print("Actuator number: "+ str(actuatorRelay1)+" On relay 1. Cicle #:" + str(counter) + '\n')
#         time.sleep(3)
#         GPIO.output(21, False)
#         time.sleep(3)


        # GPIO.output(20, True)
        # counter1 = counter1 + 1
        # print("Actuator on relay 2. Cicle #:" + str(counter1) + '\n')
        # time.sleep(3)
        # GPIO.output(20, False)
        # GPIO.output(26, True)
        # counter2 = counter2 + 1
        # print("Actuator on relay 3. Cicle #:" + str(counter2) + '\n')
        # time.sleep(3)
        # GPIO.output(26, False)

# finally:


    # cleanup the GPIO before finishing :)
    print("Actuator number "+str(actuatorRelay1)+" On relay #1 runs: " + str(counter) + " Cicles")
    print("Actuator on relay #1 run: " + str(counter1) + " Cicles")
    print("Actuator on relay #1 run: " + str(counter2) + " Cicles")
    GPIO.cleanup()
