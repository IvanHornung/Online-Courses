#Web Services

'Web-based Services'
#Services "in the cloud"
#Runs on remote server, accepts requests from clients
#Interact using HTTP messages

'Application Programming Interface'
#An API defines the communication interface between programs
#Defines the format of Request/Response messages
#Defines legal message sequences

#>> GET /maps/<place> HTTP/1.1

'Software Development Kit (SDK)'
#An SDK is a set of tools to support the use of an API
#Typically library functions
#Programmer does not need to know the message details
#API and SDK may be used interchangeably
#API is interface, SDK is set of tools

    '''
API:
GET /maps/<place> HTTP/1.1
SDK:
map = GetMap("UCI")
    '''