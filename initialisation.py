#  initialisation mode is a debugging step to ensure that all sensors, camera and motor is in working conditions

# user will do manual check on all the component before letting system to run automatically (will have an option to run this or not)

#  GPIO PIn allocation is defined in each sub functions

#  setup humidity and temperature sensor
import os
import pigpio
import DHT22
import time

os.chdir('pigpio_dht22')
pi = pigpio.pi()
s = DHT22.sensor(pi, 4)  # reading sensor from gpio pin 4

#  read threshold values from database, user keyboard input for now
# input humidity sensor threshold level
humidity_threshold = float(input("Set threshold humidity level: "))
# input temperature threshold level
temp_threshold = float(input("Set threshold temperature level: "))

s.trigger()         # trigger sensor to read value
time.sleep(1)       # time delay of 1 second
print('{:3.2f}'.format(s.humidity()/ 1.))
print('{:3.2f}'.format(s.temperature()/ 1.))
humTemp_work = int(input("Is humidity and temperature sensors working? Yes(1) or No(0): "))
if humTemp_work == 0:
    print("please check your DHT22 module operating unit and wiring.")
    while 1:


# setup rain sensor

rain = 0
import rainsensor

if rain:
    print("raining")
else:
    print("not raining")
rain_work = int(input("Is rain sensor working? Yes(1) or No(0): "))
if rain_work == 0:
    print("please check your rain sensor operating unit and wiring.")
    while 1:

#  setup pi camera

import camera

camera_work = int(input("Is pi camera working? Yes(1) or No(0): "))
if camera_work == 0:
    print("please check your pi camera module operating unit and connection.")
    while 1:

import calibration
