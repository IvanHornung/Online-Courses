'''
Use the http.client package to read the contents of the www.uci.edutop 
level web page and print out the first 3 lines. You will need to use http.client.HTTPSConnection()
to make the connection to the www.uci.edu web page. Then you will need to use conn.request("GET", "/")
to send the get request. Then use conn.getresponse() to extract the response and use the read() method
of the response to return the contents of the webpage.
'''

import http.client

conn = http.client.HTTPSConnection("www.uci.edu")
conn.request("GET", "/")
data = conn.getresponse()
message = data.read()
print(message)

#Below was attempt for first 3 lines but they are all whitespace characters (eg"\t\n\t\n"), and appeared as numbers
lineCount = 0
for line in message:
    print(repr(line))
    if lineCount > 3:
        break
    lineCount+=1