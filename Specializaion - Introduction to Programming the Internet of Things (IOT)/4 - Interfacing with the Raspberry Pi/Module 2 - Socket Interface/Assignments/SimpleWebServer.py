'''
Use the socket to write a simple web server running on your Raspberry Pi. 
When your server receives a request it should print “Got a request!” to the screen of the Raspberry Pi.
Turn in your code and turn in a screen shot of your Raspberry Pi’s screen with “Got a request!”
printed in order to demonstrate that it worked.

In order to get the screen shot, you will need to set up your Raspberry Pi, run the server,
and type the IP address of your Raspberry Pi into the address line of a web browser running on a desktop or a laptop.

'''

while True:
    import socket
    ms = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ainfo = socket.getaddrinfo(None, 1234)
    ms.bind(ainfo[4][4])
    ms.listen(5)
    conn, addr = ms.accept()
    data = conn.recv(1000)
    if data:
        print('Got a request!')
    elif not data:
        break

conn.close()
ms.close()