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
end_time = None
cap = None # to be assigned later, cv2.VideoCapture(0)
filename_base = "capture_" + str(time) + "_out"

last_frame = None


def init(output_folder = None):
    global filename_base, cap
    # Initialize hardware
    GPIO.setmode(GPIO.BOARD) # pin 1 at top left of header when USB at bottom

    GPIO.setup(IO_RIGHT, GPIO.IN) # right
    GPIO.setup(IO_LEFT, GPIO.IN) # left
    GPIO.setup(IO_FORWARD, GPIO.IN) # forward
    GPIO.setup(IO_BACK, GPIO.IN) # back
    # add entries for buttons and LEDs later
    if output_folder is not None:
        filename_base = output_folder # TODO: regex filter / replace for safety
    if not (os.path.exists('./' + filename_base)): # create in any case
        os.mkdir('./' + filename_base) # will throw OSError is existing dir

    cap = cv2.VideoCapture(0)
    #print(cap)
    # TODO: detect static (no signal) or black (receiver out)
    
    # sleep(init_delay)


def finish():
    global cap
    GPIO.cleanup() # reset all IO states
    if cap is not None:
        cap.release() # assuming it was set
    #cv2.destroyAllWindows() # no video output here


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

def getOutFile():
    # Keeping order, will still sort properly
    return './' + filename_base + '/' + str(time()) + "-" + filename_base  + "-" + getPinState()  + ".png"

def saveFrame():
    global saved_frames, last_frame    
    # removed frame counter check
    ret, frame = cap.read()
    # removed display logic here cv2.imshow('frame', frame)
    # removed if cv2.waitKey(1) & 0xFF == ord('q') / break (in try)
    last_frame = frame
    outfile = getOutFile()
    cv2.imwrite(outfile, frame)
    saved_frames =+ 1

def getLastFrame():
    return last_frame

if __name__ == '__main__':
    init("maintest")
    print(getPinState())
    saveFrame()
    print(last_frame)



atexit.register(finish)
