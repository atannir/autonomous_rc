import RPi.GPIO as GPIO
from time import sleep

# "Constants"
IO_RIGHT = 3
IO_LEFT = 5
IO_FORWARD = 8
IO_BACK = 10

buttons = [IO_RIGHT, IO_LEFT, IO_FORWARD, IO_BACK]

duration = 0.15

GPIO.setmode(GPIO.BOARD) # pin 1 top left of header

GPIO.setup(IO_RIGHT, GPIO.OUT) # right
GPIO.output(IO_RIGHT, GPIO.HIGH) # reset needed for 4x4
GPIO.setup(IO_LEFT, GPIO.OUT) # left
GPIO.output(IO_LEFT, GPIO.HIGH) # reset needed for 4x4
GPIO.setup(IO_FORWARD, GPIO.OUT) # forward
GPIO.output(IO_FORWARD, GPIO.HIGH) # reset needed for 4x4
GPIO.setup(IO_BACK, GPIO.OUT) # back
GPIO.output(IO_BACK, GPIO.HIGH) # reset needed for 4x4

# may need to examine wiring again
# manually setting HIGH for back and right only

pattern = [["L", duration],
           ["R", duration],
           ["F", duration],           
           ["B", duration],
#           ["S", duration],
#           ["N", duration]
           ]

def dirWithDur(direction = 0, duration = 0.0):
    # pass in 0 to 2 in alphabet of (FNB)(RSL)
    # if called with no args, unpress all buttons
    print(str(direction) + " " + str(duration))
    if (direction == 0):
        for b in buttons:
            GPIO.output(b, GPIO.HIGH) # button off
            #sleep(duration)
        sleep(duration)
        return
    if "S" in direction: # straight, no turning
        GPIO.output(IO_FORWARD, GPIO.HIGH)
        GPIO.output(IO_BACK, GPIO.HIGH)
    if "N" in direction: # neutral motion
        GPIO.output(IO_LEFT, GPIO.HIGH)
        GPIO.output(IO_RIGHT, GPIO.HIGH)
    if "F" in direction: # and "B" not in direction:
        GPIO.output(IO_FORWARD, GPIO.LOW)
        GPIO.output(IO_BACK, GPIO.HIGH)
    if "B" in direction: # and "F" not in direction:
        GPIO.output(IO_BACK, GPIO.LOW)
        GPIO.output(IO_FORWARD, GPIO.HIGH)
    if "R" in direction: # and "L" not in direction:
        GPIO.output(IO_RIGHT, GPIO.LOW)
        GPIO.output(IO_LEFT, GPIO.HIGH)
    if "L" in direction: # and "R" not in direction:
        GPIO.output(IO_LEFT, GPIO.LOW)
        GPIO.output(IO_RIGHT, GPIO.HIGH)
    sleep(duration)

try:
    for (d, dur) in pattern:
        dirWithDur(d, dur)
#    dirWithDur("B", 0.15)
#    dirWithDur()

finally:
    GPIO.cleanup()
