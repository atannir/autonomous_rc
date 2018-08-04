import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)

def getDutyCycle(angle):
    #k = (1+(float(angle)/180))/20
    return (angle / 18) + 2
    #GPIO.output(11,True)
    #pwm.ChangeDutyCycle(duty)
    pwm.ChangeDutyCycle(0)
    #return(k)

def pointAndDelay(angle, time = 1):
    duty = getDutyCycle(angle)
    GPIO.output(11,True)
    pwm.ChangeDutyCycle(duty)
    print(angle, " - ", duty)
    sleep(time)
    GPIO.output(11,False)
    pwm.ChangeDutyCycle(0)


pwm = GPIO.PWM(11,50) # 50 Hz

GPIO.output(11,True)
pwm.start(0)

pointAndDelay(0, 1)
pointAndDelay(90, 1)
pointAndDelay(180, 1)
pointAndDelay(90, 1)


GPIO.output(11,False)

pwm.stop()

GPIO.cleanup()

