import cv2
import numpy as np
import atexit

cap = None

last_frame = None

def init():
    global cap
    cap = cv2.VideoCapture(0)

def returnFrame():
    global last_frame
    ret, frame = cap.read()
    # should check ret for true
    last_frame = frame
    return frame
    
def finish():
    cap.release()

atexit.register(finish)
