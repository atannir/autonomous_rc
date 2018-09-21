import RPi.GPIO as GPIO
from time import time, sleep
import numpy as np
import cv2 # display

import redcar as car
#import state_recorder as ctl



# drive car with keyboard

car.init()
#ctl.init()
# Double cleanup error but whatever

car.setCmd("FL", 0.3)
car.go()
