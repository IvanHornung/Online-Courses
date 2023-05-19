#Live Server

'''Sending and Receiving'''
data = conn.recv(1000)
conn.sendall(data)

conn.close()
mysock.close()
#recv() and sendall() used to send and receive data
#Connection and socket close separately

'''A Live Server'''
while True:
    conn, addr = mysock.accept()
    data = conn.recv(1000)
    if not data:
        break
    conn.sendall(data)

conn.close()
mysock.close()

#An infinite loop is typical
#Connection close when no data is received

'''Full Server Program'''

import socket
import sys

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    mysock.bind("", 1234)
except socket.error:
    print("Failed to bind")
    sys.exit()
mysock.listen(5)
while True:
    conn, addr = mysock.accept()
    data = conn.recv(1000)
    if not data:
        break
    conn.sendall(data)

conn.close()
mysock.close()