#General Purpose IO Pins (Updated)

'''Pin Direction and Assignment'''
GPIO.setup(13, GPIO.OUT)
#Set the pin directions
#Like pinMode(13, OUTPUT) for Arduino

GPIO.output(13, True)
#Assign value to output pin
#Like digitalWrite(11, HIGH) for Arduino

'''Blink an LED'''
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.OUT)
while True:
    GPIO.output(13, True)
    time.sleep(1)
    GPIO.output(13, False)
    time.sleep(1)

'''Reading Input Pins'''
GPIO.setup(13, GPIO.IN)
#Set the pin direction to an input

vlaue = GPIO.input(13)
#Read value on input pin
#Only reads digital inputs
#   -No analogRead equivalent
#   -No analog-to-digital converter
