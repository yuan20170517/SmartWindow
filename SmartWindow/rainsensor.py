from time import sleep
import os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN)
state = GPIO.input(18)

while(1):

    if (state == 0):
        print "It is raining."
    else:
        print "It is not raining."

    sleep(5)

