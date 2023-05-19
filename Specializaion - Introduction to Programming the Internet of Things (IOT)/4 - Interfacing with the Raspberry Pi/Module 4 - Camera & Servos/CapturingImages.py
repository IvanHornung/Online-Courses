#Capturing Images
import socket
import picamera
'Sending an Image on the Network'
#What if you want to a remote site?
#   -Home security system
#Capturing an image, send it on a connection

mysock = socket.socket()
mysock.connect(('aserver', 8000))
conn = mysocket.makefil('wb') #makes file object in global directory; wb are permissions: you can write to this file
camera.capture(conn, 'jpeg') 
#Need a file-like object to capture to

'Timelapse Photography'
camera.capture_continuous() #takes photos over time
#Takes one argument, a file name
# {counter} and {timestamp} can be substituted
#ex. "picture{counter}.jpg" produces picture1.jpg, picture2.jpg, etc.

'Continuous Capture'
camera = picamera.PiCamera()
for filename in camera.capture_continuous('img{counter}.jpg'):
    time.sleep(300)
#iterate through all images
#   -infinite loop
#5 minute delay between images
