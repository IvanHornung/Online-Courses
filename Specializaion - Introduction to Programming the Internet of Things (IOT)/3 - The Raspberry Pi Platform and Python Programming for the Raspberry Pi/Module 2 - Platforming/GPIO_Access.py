#GPIO Access

'''Importing GPIO Library'''
import Rpi.GPIO as GPIO

'''Selecting Pin Numbering Mode'''
GPIO.setmode(GPIO.BOARD)
#Use board numbering

GPIO.setmode(GPIO.BCM)
#Use Broadcom SoC numbering
#Changes with different versions of Raspberry Pi
