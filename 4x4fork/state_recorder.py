from time import sleep, time
import cv2
import os
import atexit

import image_capture as img
import controller_capture as ctl

# Defaults

init_delay = 5 # feels like a long time if you are waiting
saved_frames = 0
frame_delay = 0.1 # 20 fps 0.05, 10 fps = 0.1
max_frames = 500
start_time = time()

filename_base = "capture_" + str(time()) + "_out"

last_frame = None
last_frame_time = time() # Not ideal but will avoid type error with None
end_time = None

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
    global saved_frames, last_frame, last_frame_time
    # removed frame counter check
    # removed display logic here cv2.imshow('frame', frame)
    # removed if cv2.waitKey(1) & 0xFF == ord('q') / break (in try)
    frame = img.returnFrame()
    last_frame = frame
    last_frame_time = time()
    outfile = getOutFile()
    cv2.imwrite(outfile, frame)
    saved_frames =+ 1

def getLastFrame():
    return last_frame

if __name__ == '__main__':
    #init("maintest")
    init()
    #print(ctl.getPinState())
    saveFrame() #make sure there is 1 frame changed and times are updated
    while ((saved_frames <= max_frames) and (cv2.waitKey(1) & 0xFF != ord('q') )):
        # will waitKey work if we don't have a display window?
        cv2.imshow('feed', img.returnFrame())
        print( str(time()) + " " + str(last_frame_time) + " " + str(last_frame_time + frame_delay))
        if((last_frame_time + frame_delay) < time()):
            saveFrame()
        #pass
        sleep(0.01) # try not to peg the CPU displaying frames

atexit.register(finish)
