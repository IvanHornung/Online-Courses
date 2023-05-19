#Pulse Width Modulation

import RPi.GPIO as GPIO
import time

'''PWN Initialization'''
pwm_obj = GPIO.PWN(18, 400)
#Mark pin for PWN
#Second argument is frequency

pwm_obj.start(100)
#Start generating PWN signal
#Argument is duty cycle, 0 to 100

'''PWN Control'''
pwm_obj.ChangeDutyCycle(50)
#Assign new duty cycle
#PWN frequency is not accurate
#   -Off by over 50% at 10kHz

'''Frequency Control'''
#Cannot easily control frequency
#   -No tone() function as on Arduino
#Need to do it manually

while True:
    GPIO.output(18, True)
    time.sleep(0.5)
    GPIO.output(18, False)
    time.sleep(0.5)
#1Hz frequency
