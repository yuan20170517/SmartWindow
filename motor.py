# GPIO 17–Pin 22 > L293D–Pin 1 Vcc1
# GPIO 21–Pin 18 > L293D–Pin 2 1A
# GPIO 22–Pin 16 > L293D–Pin 7 2A

# Motor–wire 1 > L293D–pin 3 PWM1 to 1Y
# Motor–wire 2 > L293D–pin 6 PWM2 to 2Y
# 12V -wire 3  > L293D–pin 8   Vcc2
# Wire 4       >  L293D–pin 4 GND
# Wire 5       >  L293D–pin 5 GND

# modify from https://business.tutsplus.com/tutorials/controlling-dc-motors-using-python-with-a-raspberry-pi--cms-20051
# access a module called RPi.GPIO which turning the GPIO pins on and off
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)  # board numbering on the Raspberry Pi

Motor1A = 17
Motor1B = 21
Motor1E = 22

GPIO.setup(Motor1A, GPIO.OUT)
GPIO.setup(Motor1B, GPIO.OUT)
GPIO.setup(Motor1E, GPIO.OUT)

inst = int(input("instruction to turn motor clockwise(0) or anticlockwise(1) or stop(2): "))
tach = 100

if inst == 0:
    print("Turning motor clockwise")
    GPIO.output(Motor1A, GPIO.HIGH)
    GPIO.output(Motor1B, GPIO.LOW)
    GPIO.output(Motor1E, GPIO.HIGH)
    while 1:
        tach -= 1
        if tach == 0:
            break

elif inst == 1:
    print("Turning motor anticlockwise")
    GPIO.output(Motor1A, GPIO.HIGH)
    GPIO.output(Motor1B, GPIO.LOW)
    GPIO.output(Motor1E, GPIO.HIGH)
    while 1:
        tach -= 1
        if tach == 0:
            break

elif inst == 2:
    print("Stop motor")
    GPIO.output(Motor1A, GPIO.HIGH)
    GPIO.output(Motor1B, GPIO.LOW)
    GPIO.output(Motor1E, GPIO.LOW)
    while 1:
        tach -= 1
        if tach == 0:
            break
GPIO.cleanup()
