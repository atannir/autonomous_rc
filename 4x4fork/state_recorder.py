import RPi.GPIO as GPIO
from time import sleep, time
import numpy as np
import cv2
import os
import atexit

# "Constants"
IO_RIGHT = 5
IO_LEFT = 7
IO_FORWARD = 8
IO_BACK = 10

# Defaults

init_delay = 5 # feels like a long time if you are waiting
saved_frames = 0
frame_delay = 0.05
max_frames = 100
start_time = time()
cap = None # to be assigned later, cv2.VideoCapture(0)



def init(output_folder = ""):
    # Initialize hardware
    GPIO.setmode(GPIO.BOARD) # pin 1 at top left of header when USB at bottom

    GPIO.setup(IO_RIGHT, GPIO.IN) # right
    GPIO.setup(IO_LEFT, GPIO.IN) # left
    GPIO.setup(IO_FORWARD, GPIO.IN) # forward
    GPIO.setup(IO_BACK, GPIO.IN) # back
    # add entries for buttons and LEDs later
    sleep(init_delay)

def finish():
    GPIO.cleanup() # reset all IO states
    cap.release() # assuming it was set
    #cv2.destroyAllWindows() # no video output here

def getPinState():
    # forward, neutral, back
    # left, straight, right
    outstr = ""
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
                              

    
atexit.register(finish)
