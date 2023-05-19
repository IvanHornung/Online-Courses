#Python Server Demo

#-------------Server
pi@raspberrypi:~ $ python3
>>> import socket
>>> ms = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
>>> ainfo = socket.getaddrinfo(None, 1234)
>>> print(ainfo)
>>> ms.bind(ainfo[0][4]) || ms.bind(('127.0.0.1',1234))
>>> ms.listen(5)
>>> conn, addr = ms.accept()
>>> data = conn.recv(1000)
>>> print(data)
b'hello world\n'
>>> conn.close()
>>> ms.close()

#----------Sender
pi@raspberrypi:~ $ nc 127.0.0.1 1234
hello world