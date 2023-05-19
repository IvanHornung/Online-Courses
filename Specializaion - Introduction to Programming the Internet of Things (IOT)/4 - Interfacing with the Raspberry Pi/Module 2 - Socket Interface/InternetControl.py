#Internet Control
import socket
import RPi.GPIO as GPIO

'''Control via the Internet'''
#Controlling a device over the Internet is interesting
#   -Home automation
#   -Tele-medicine
#Sends commands to a Raspberry Pi
#Rpi does something in the real world
#Sensor data can be sent remotely

'''Internet Controlled LED'''
#PHONE->CLOUD->RPI->LED
#LED turns off and on by remote commands
#Send "on" message to turn LED on
#Send "off" message to turn LED off
#Modify server program to control LED

'''Modified Server Program'''
while True:
    conn, addr = mysock.accept()
    data = conn.recv(1000)
    if not data:
        break
    if data == b'on':
        GPIO.output(13, True)
    if data == b'off':
        GPIO.output(13, False)

#Received data is compared to commands
#Data is a byte array, not a string
