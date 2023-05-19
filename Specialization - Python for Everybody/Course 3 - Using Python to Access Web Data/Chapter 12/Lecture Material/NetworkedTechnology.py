'''--Transport Control Protocol (TCP)--
Built on top of IP (Internet Port)
Assume IP might lose some data - stores and retransmits data if it seems to be lost
Handles "flow control" using a transmit window
Provides a nice reliable pipe
    
--TCP Connections / Sockets--
"In computer networking, an Internet socket or network socket is an endpoint of a bidirectional inter-process
communication flow across an Internet Protocol-based computer network, such as the Internet"

Process<--Internet-->Process

--TCP Port Numbers--
-A port is an application-specific or process-specific software communications endpoint
-It allows multiple networked applications to coexist on the same server
-There is a list of well-known TCP port numbers

--Common TCP Ports--
Telnet(23) - Login          IMAP (143/220/993) - Mail Retrieval
SSH (22) - Secure Login     POP (109/110) - Mail Retrieval
HTTP (80)                   DNS (53) - Domain Name
HTTPS (443) - Secure        FTP (21) - File Transfer
SMTP (25) (Mail)            
    '''

'Sockets in Python'
#Python has built-in support for TCP Sockets

import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #hook a thing across the internet, connection point that has not been connected. STREAM = series of characters that just keep coming back
mysock.connect( ('data.pr4e.org', 80)) #Host, Port
#this doesn't send any data, it's like dialling the phone
