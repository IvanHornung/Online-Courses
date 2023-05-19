'Application Protocol'
#Since TCP (and Python) gives us a reliable socket, what do we want to do with the socket? What problems do we want to solve?
#Application Protocols
#   Mail
#   World Wide Web

'HTTP - Hypertext Transfer Protocol'
#The dominant Application Layer Protocol on the Internet
#Invented for the Web - to Retrieve HTML, Images, Documents, etc
#Extended to be data in addition to documents - RSS, Web Services, etc.. Basic Concept - Make a Connection - Request a document - Retrieve the Document - Close the connection

'HTTP'
#The HyperText Transfer Protocol is the set of rules to allow browsers to retrieve web documents from servers over the Internet

'What is a Protocol?'
#A set of rules that all parties follow so we can predict other's behavior
#And not bump into each other
#   -On two-way roads in the US, drive on the right-hand side of the road
#   -On two-way roads in the UK, drive on the left-hand side of the road

'Uniform Resource Locator'
#http://www.dr-chuck.com/page1.htm
#protocol     host       document

'Getting Data From The Server'
#Each the user cliks on an anchor tag with an href= value to switch to a new page, the browser makes a connection
#to the web server and issues a "GET" request - to GET the content of the page at the specified URL
#The server returns the HTML document to the Browser which formats and displays the document to the user

'Internet Standards'
#The standards for all the Internet protocols (inner workings) are develioped by an organization
#Internet Engineering Task Force (IETF)
#www.ietf.org
#Standards are called "RCFs" - "Request for Comments"

'Making an HTTP request'
#Connect to the server like www.dr-chuck.com
#Request a document (or the default document)
#   - GET http://www.dr-chuck.com/page1.htm HTTP/1.0
#   - GET http://www.mlive.com/ann-arbor/ HTTP/1.10
#   - GET http://www.facebook.com HTTP/1.0

#you need to have telnet installed. It's a way to connect to any port on any server in an insecure manner and send stuff to it
'''What you would tell your computer

    $telnet data.pr4e.org 80    #!telnet + host + port
    Trying 74.208.28.177...
    Connected to data.pr4e.org.Escape character is '^]'.
    #GET http://data.pr4e.org/page1.htm HTTP/1.0 #! must type this in quicky, and exactly

    The first thing you'll get is the metadata
    And then a blankline
    And then the content of the file.
    And then the connect is closed.
'''

#! An HTTP Request in Python
import socket #import a socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Like a doorway out of your computer but it's not open or connected yet
mysock.connect(('data.pr4e.org', 80) )#connect the socket. When this line is done, we have a socket that is connected to a server. 
#you do know that the server is there and you know there's software on the other end of it, otherwise the connect will fail
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode() #now you can send messagesor recieve. characters = ENTER x2
mysock.send(cmd) #server does a recieve first and you do a send first

while True :
    data = mysock.recv(512) #receive method. receive up to 512 characters
    if(len(data) < 1) : #if we get no data, that means end of file
        break #or end of transmission
    print(data.decode()) #if we did get data, we decode it. taking data from the outside world and interpreting what
                            #it means internally for us
mysock.close()
#OP: same as from Telnet
