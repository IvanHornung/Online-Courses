#Tweet Response

'Filtering Twitter Streams'
class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            print('Found it.')

stream = MyStreamer(C_KEY, C_SECRET, A_TOKEN, A_SECRET)
stream.statuses.filter(track="Hornung")
#Create the MyStreamer class
#Callback prints a result
#Instantiate MyStreamer
#Filter the stream to find the text


'Blinking in Response to a Tweet'

import RPi.GPIO as GPIO
import time

def blink():
    GPIO.output(13, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(13, GPIO.LOW)

class MyStreamer(TwythonStreamer):
    def on_success(self data):
        if 'text' in data:
            blink()
#Let's make an LED blink when a tweet is received.
#LED is on pin 13.