#Python Client Demo

#-------------Sending port
pi@raspberrypi:~ $ ls
pi@raspberrypi:~ $ python3

>>> import socket
>>> ms = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
>>> ms.connect(("127.0.0.1", 1234)) #(IP, port#); IP = loopback address (sending to itself)
>>> ms.sendall(b"Hello world!")
>>> ms.sendall(b"Hello again!")

#-------------Receiving port

pi@raspberrypi:~ $ nc -l 1234
Hello world!Hello again!