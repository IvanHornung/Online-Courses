'''
Connect an LED to your Raspberry Pi and write a program to gradually increase brightness,
and then gradually decrease brightness. The exact rate of increase and decrease is not
critical but let it take at least one second to go from maximum to minimum brightness.
Be sure to use pulse width modulation to change the brightness of the LED. Also,
be sure to wire the LED in series with an appropriate resistor so that it does not receive too much current.

Turn in your code and a link to a video of your system with the LED brightness changing.
'''

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
pwm = GPIO.PWM(12, 50)
pwm.start(0)

while True:
    for i in range(100):
        pwm.ChangeDutyCycle(i)
        time.sleep(0.1)
    for i in range(100, 0, -1):
        pwm.ChangeDutyCycle(i)
        time.sleep(0.1)