import cv2
import os
#from time import sleep, time
import time
import numpy as np

# open capture device, capture frame to numpy, save, deinterlace, save again

start = time.time()
time.sleep(0.5)
print(time.time() - start)

# from py_video_display.html from official OpenCV3 beta docs

cap = cv2.VideoCapture(0) # assume it does the right thing
#cap = cv2.CaptureVideo(0)
time.sleep(0.5)
cap.release()

#while(True):
    # Capture frame by frame
#    ret, frame(
