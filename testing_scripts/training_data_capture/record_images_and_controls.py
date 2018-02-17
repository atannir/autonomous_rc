import RPi.GPIO as GPIO
from time import sleep, time
import numpy as np
import cv2
import os

# "Constants"
IO_RIGHT = 3
IO_LEFT = 5
IO_FORWARD = 8
IO_BACK = 10

# Configuration
# TODO enable setting with command line arguments
init_delay = 5
max_frames = 200
frame_delay = 0.05
filename_base = 'doortomain1'
display_frame = True

# Other variables
saved_frames = 0
start_time = time()

# Initialize hardware
GPIO.setmode(GPIO.BOARD) # pin 1 at top left of header when USB at bottom

GPIO.setup(IO_RIGHT, GPIO.IN) # right
GPIO.setup(IO_LEFT, GPIO.IN) # left
GPIO.setup(IO_FORWARD, GPIO.IN) # forward
GPIO.setup(IO_BACK, GPIO.IN) # back

# claim capture device
cap = cv2.VideoCapture(0)

if not (os.path.exists('./' + filename_base)):
    os.mkdir('./' + filename_base) # will throw OSError if exists

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

def getOutFile():
    return './' + filename_base + '/' + str(time()) + "-" + filename_base  + "-" + getPinState()  + ".png"

# Main loop for button state read and image capture
print("Sleeping for " + str(init_delay) + " seconds")
sleep(init_delay)

try:
    while(saved_frames < max_frames):
        ret, frame = cap.read()

        #Display captured frame if display set
        if(display_frame):
            cv2.imshow('frame', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'): # needed for 64-bit systems
            break
        #pinState = getPinState()
        # print(pinState + " - " + getPinState()) # no diff in tests
        outfile = getOutFile()
        print(outfile)
        cv2.imwrite(outfile, frame)
        saved_frames += 1
        sleep(frame_delay)
        
finally:
    GPIO.cleanup() # reset all IO states
    cap.release() # free capture device
    cv2.destroyAllWindows() # clean up all GUI elements


# Helpful sources:
#
# GPIO:
# https://stackoverflow.com/questions/46106989/how-to-record-button-presses-in-python-to-open-combination-lock
# https://sourceforge.net/p/raspberry-gpio-python/wiki/Inputs
#
# OpenCV capture / writing:
#
# From official documentation https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html
