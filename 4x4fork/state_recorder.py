from time import sleep, time
import cv2
import os
import atexit

import image_capture as img
import controller_capture as ctl

# Defaults

init_delay = 5 # feels like a long time if you are waiting
saved_frames = 0
frame_delay = 0.05
max_frames = 100
start_time = time()
end_time = None

filename_base = "capture_" + str(time()) + "_out"

last_frame = None


def init(output_folder = None):
    global filename_base #, cap
    img.init()
    # Initialize hardware
    ctl.init()

    if output_folder is not None:
        filename_base = output_folder # TODO: regex filter / replace for safety
    if not (os.path.exists('./' + filename_base)): # create in any case
        os.mkdir('./' + filename_base) # will throw OSError is existing dir

    # init delay here


def finish():
    pass


def getOutFile():
    # Keeping order, will still sort properly
    return './' + filename_base + '/' + str(time()) + "-" + filename_base  + "-" + ctl.getPinState()  + ".png"

def saveFrame():
    global saved_frames, last_frame    
    # removed frame counter check
    # removed display logic here cv2.imshow('frame', frame)
    # removed if cv2.waitKey(1) & 0xFF == ord('q') / break (in try)
    frame = img.returnFrame()
    last_frame = frame
    outfile = getOutFile()
    cv2.imwrite(outfile, frame)
    saved_frames =+ 1

def getLastFrame():
    return last_frame

if __name__ == '__main__':
    init("maintest")
    print(ctl.getPinState())
    saveFrame()

atexit.register(finish)
