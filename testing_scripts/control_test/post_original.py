import RPi.GPIO as GPIO
import time



GPIO.setmode(GPIO.BOARD) # pin 1 top left of header

GPIO.setup(3, GPIO.OUT) # right
GPIO.setup(5, GPIO.OUT) # left
GPIO.setup(8, GPIO.OUT) # forward
GPIO.setup(10, GPIO.OUT) # back

try:
    GPIO.output(3, GPIO.LOW)
    time.sleep(0.2)
    GPIO.output(3, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(5, GPIO.LOW)
    time.sleep(0.2)
    GPIO.output(5, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(8, GPIO.LOW)
    time.sleep(0.2)
    GPIO.output(8, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(10, GPIO.LOW)
    time.sleep(0.2)
    GPIO.output(10, GPIO.HIGH)
    time.sleep(0.2)

finally:
    GPIO.cleanup()
