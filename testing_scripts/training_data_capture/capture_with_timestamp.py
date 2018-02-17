import numpy as np
import cv2
from time import sleep, time
import os

# Testing script. Successfully runs on python 2 and capture device
# From official documentation https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html

max_frames = 5
#frame_delay = 0.1 # 100 in about 14 seconds - 7 fps with cpu to spare
frame_delay = 0.05 # 100 in 8.5 s - 11 fps
#frame_delay = 0.0 # 100 in about 3.5 seconds - 28 fps, essentially real time 
saved_frames = 0

start_time = time()

filename_base = 'test' # is also directory

# end config, begin code
#if not (os.path.exists('./' + filename_base)):
#   os.mkdir('./' + filename_base) # will throw OSError if exists
# if(os.path.isdir('./' + filename_base):

cap = cv2.VideoCapture(0)

while(saved_frames < max_frames):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display resulting frame
    cv2.imshow('frame', frame)
    # cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    print(saved_frames)
    print(time() - start_time)
    outfile = './' + filename_base + '/' + str(time()) + "-" + filename_base  + "-" + "FNBLSR.png"
    print(outfile)
    cv2.imwrite(outfile, frame)
    # forward, neutral, back, left, straight, right
    saved_frames += 1
    sleep(frame_delay)

# When done, release capture
cap.release()
cv2.destroyAllWindows()
