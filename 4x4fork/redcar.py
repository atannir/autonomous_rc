import RPi.GPIO as GPIO
from time import sleep
import atexit

# module for the red remote control car
# later use this kind of framework for loading configuration files
# into generic car objects
#
#

# "Constants"
IO_RIGHT = 5
IO_LEFT = 7
IO_FORWARD = 8
IO_BACK = 10

buttons = [IO_RIGHT, IO_LEFT, IO_FORWARD, IO_BACK]

# Defaults

default_duration = 0.2 # in seconds

# State variables

last_cmd = ""
current_cmd = ""
next_cmd = ""

debug = True
debug = False


def init():
    GPIO.setmode(GPIO.BOARD) # pin 1 top left of header
    GPIO.setup(IO_RIGHT, GPIO.OUT) # right
    GPIO.output(IO_RIGHT, GPIO.HIGH) # reset needed for 4x4
    GPIO.setup(IO_LEFT, GPIO.OUT) # left
    GPIO.output(IO_LEFT, GPIO.HIGH) # reset needed for 4x4
    GPIO.setup(IO_FORWARD, GPIO.OUT) # forward
    GPIO.output(IO_FORWARD, GPIO.HIGH) # reset needed for 4x4
    GPIO.setup(IO_BACK, GPIO.OUT) # back
    GPIO.output(IO_BACK, GPIO.HIGH) # reset needed for 4x4

def finish():
    GPIO.cleanup()

def testAllOutputs():
    forward()
    backward()
    stop(0.5)
    left()
    right()
    stop(0.5)

def dprint(s):
    if debug:
        print(s)
    
def dirWithDur(direction = 0, duration = 0.0):
    # pass in 0 to 2 in alphabet of (FNB)(RSL)
    # if called with no args, unpress all buttons
    dprint(str(direction) + " " + str(duration))
    if (direction == 0):
        for b in buttons:
            GPIO.output(b, GPIO.HIGH) # button off
            #sleep(duration)
        sleep(duration)
        return
    if "S" in direction: # straight, no turning
        GPIO.output(IO_LEFT, GPIO.HIGH)
        GPIO.output(IO_RIGHT, GPIO.HIGH)
        dprint("Straight")
    if "N" in direction: # neutral motion
        GPIO.output(IO_FORWARD, GPIO.HIGH)
        GPIO.output(IO_BACK, GPIO.HIGH)
        dprint("Neutral")
    if "F" in direction: # and "B" not in direction:
        GPIO.output(IO_FORWARD, GPIO.LOW)
        GPIO.output(IO_BACK, GPIO.HIGH)
        dprint("Going F")
    if "B" in direction: # and "F" not in direction:
        GPIO.output(IO_BACK, GPIO.LOW)
        GPIO.output(IO_FORWARD, GPIO.HIGH)
        dprint("Going B")
    if "R" in direction: # and "L" not in direction:
        GPIO.output(IO_RIGHT, GPIO.LOW)
        GPIO.output(IO_LEFT, GPIO.HIGH)
        dprint("Turning R")
    if "L" in direction: # and "R" not in direction:
        GPIO.output(IO_LEFT, GPIO.LOW)
        GPIO.output(IO_RIGHT, GPIO.HIGH)
        dprint("Turning L")
    sleep(duration)

def stop(duration = 0):
    dirWithDur(0, duration)

def left(duration = default_duration):
    dirWithDur("L", duration)

def right(duration = default_duration):
    dirWithDur("R", duration)

def forward(duration = default_duration):
    dirWithDur("F", duration)

def backward(duration = default_duration):
    dirWithDur("B", duration)

if __name__ == "__main__":
    print("Debug: " + str(debug))
    print("Testing module for red RC car.")
    init()
    testAllOutputs()
    # finish()
    
#finally:
#    GPIO.cleanup()
atexit.register(finish)
