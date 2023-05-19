#Sever Code
import socket

'''Sockets on the Server'''
#Server needs to wait for requests
#1. Create a socket
#2. Bind the socket to an IP address and port
#3. Listen for a connection
#4. Accept the connection
#5. Receive the request
#6. Send the response

'''Creating and Binding a Socket'''
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.bind("", 1234)
#-bind() binds the socket to a port
#-First argument is the host, it is empty
#   -Can receive from any host
#-Port number is arbitrary and not well-known

'''Listening and Accepting a Connection'''
mysock.listen(5)
conn, addr = mysock.accept()
#listen() starts listening for a connect()
#   -Argument is backlog, number of requests allowed to wait for a service
#accept() accepts a connection request
#   -Returns a connection (for sending/receiving) and an addres (IP, port)
