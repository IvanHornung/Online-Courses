#Exceptions

'''Handling Exceptions'''
#When an error happens, you mighr want your code to do somethign appropriate
#Use try and except statements
#Place code with possible error inside the try clause
#Code in the execpt clause is executed when an exception occurs
try:
    z = x / y
except ZeroDivisionError:
    print("Divide by zero")

'''Socket Exceptions'''
#socket.error
#   -All socket errors
#gaierror
#   -getaddressinfo() error - no host found
#We will handle some of these to make the networking more robust to errors

'''Client Program'''

import socket
import sys

try:
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print('Failed to create socket')
    sys.exit()
try:
    host = socket.gethostbyname('www.google.com')
except socket.gaierror:
    print('Failed to get host')
    sys.exit()
mysock.connect((host, 80))
message = "GET / HTTP/1.1\r\n\r\n"
try:
    mysock.sendall(message)
except socket.error:
    print('Failed to send')
    sys.exit()
data = mysock.recv(1000)
print(data)
mysock.close()