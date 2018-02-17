import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD) # pin 1 top left of header

# https://stackoverflow.com/questions/46106989/how-to-record-button-presses-in-python-to-open-combination-lock
# https://sourceforge.net/p/raspberry-gpio-python/wiki/Inputs

GPIO.setup(3, GPIO.IN) # right
GPIO.setup(5, GPIO.IN) # left
GPIO.setup(8, GPIO.IN) # forward
GPIO.setup(10, GPIO.IN) # back

try:
    for i in range(5000):
        # read state and time, triggered by interrupts and pin change
        if (GPIO.input(3) == False):
            print("right")
        if (GPIO.input(5) == False):
            print("left")
        if (GPIO.input(8) == False):
            print("forward")
        if (GPIO.input(10) == False):
            print("back")
        sleep(0.01)

finally:
    GPIO.cleanup()
