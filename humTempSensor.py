import os
import pigpio
import DHT22
import time

os.chdir('pigpio_dht22')
pi = pigpio.pi()
s = DHT22.sensor(pi, 4)

for x in range (0,10):  # loop of x from 0 to 10
    s.trigger()         # trigger sensor to read value
    time.sleep(1)       # time delay of 1 second
    print('{:3.2f}'.format(s.humidity()/ 1.))
    print('{:3.2f}'.format(s.temperature()/ 1.))
