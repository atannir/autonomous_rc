import RPi.GPIO as GPIO
from time import sleep, time
import os
import atexit

# "Constants"
IO_RIGHT = 5
IO_LEFT = 7
IO_FORWARD = 8
IO_BACK = 10

def init():
    GPIO.setmode(GPIO.BOARD) # pin 1 at top left of header when USB at bottom

    GPIO.setup(IO_RIGHT, GPIO.IN) # right
    GPIO.setup(IO_LEFT, GPIO.IN) # left
    GPIO.setup(IO_FORWARD, GPIO.IN) # forward
    GPIO.setup(IO_BACK, GPIO.IN) # back

def getPinState():
        # forward, neutral, back
        # left, straight, right
        outstr = ""
        if((GPIO.input(IO_FORWARD) == False) and
           (GPIO.input(IO_BACK) == False) and
           (GPIO.input(IO_RIGHT) == False) and
           (GPIO.input(IO_LEFT) == False)):
            return "XY" # remote off
        if (GPIO.input(IO_FORWARD) == False):
            outstr += "F"
        elif (GPIO.input(IO_BACK) == False):
            outstr += "B"
        else:
            outstr += "N"

        if (GPIO.input(IO_RIGHT) == False):
            outstr += "R"
        elif (GPIO.input(IO_LEFT) == False):
            outstr += "L"
        else:
            outstr += "S"
        return outstr
                                                    
                                            
def finish():
    GPIO.cleanup()

atexit.register(finish)
