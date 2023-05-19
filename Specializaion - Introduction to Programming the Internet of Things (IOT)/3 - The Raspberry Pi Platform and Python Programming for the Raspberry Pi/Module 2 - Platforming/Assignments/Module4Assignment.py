
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)
GPIO.setup(12, GPIO.OUT)

GPIO.output(12, False)

while True:
  while not GPIO.input(11):
    print('button pressed')
    GPIO.output(12, GPIO.HIGH)
    time.sleep(0.2)
  else:
    GPIO.output(12, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(12, GPIO.LOW)
    time.sleep(0.1)
    print('button not pressed')
