#Networking Libraries

'''Networking Libraries'''
#The Socket library is very low-level
#Programmer composes the message content
#Must know details of the protocol

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostbyname('www.google.com')
mysock.conncet(host, 80)
message = "GET / HTTP/1.1\r\n\r\n"
mysock.sendall(message)

'''Protocol-Specific Libaries'''
#Other libraries available for specific protocols
#Programmer does not need to know protocol details
#Library functions are provided to handle details

import http.client
conn = httplib.HTTPConnection("www.google.com")
conn.request("GET", "/")

'''Interaction with Online Services'''
#Many services exist which you can use programmatically
#   -Google Maps
#   -Twitter
#   -YouTube
#   -Facebook