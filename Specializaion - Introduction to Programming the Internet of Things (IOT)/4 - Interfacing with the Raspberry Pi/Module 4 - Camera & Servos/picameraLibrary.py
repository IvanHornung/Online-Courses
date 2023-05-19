#picamera Library

'python-picamera library' 
'''
sudo apt-get update
sudo apt-get install python3-picamera
'''
#Using the library
import picamera
#Instantiate an object of the PiCamera class
camera = picamera.PiCamera()

'Camera Functions'
#Take a picture
camera.capture('pict.jpg') #saves picture with provided file name

#Changing camera settings (there are many)
camera.hflip = True #horizontal flip
camera.vflip = True
camera.brightness = 50
camera.sharpness = 0

#View video on RPi screen
camera.start_preview()
camera.stop_preview()


'Video Recording'
import picamera
import time

camera.start_recording('vid.h264')
time.sleep(10)
camera.stop_recording()

' '