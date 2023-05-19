'ASCII'
#American Standard Code for Information Interchange
#this number = this letter
#In the 1960s and 1970s, we just assumed that one byte was one character

'Representing Simple Strings'
#Each character is represented by a number between 0 and 256 stored in 8 bits of memory
#We refer to "b8 bits of memory" as a "byte" of memory - (ie my disk drive contains 3 Terabytes of memory)
#The ord() function tells us the numeric value of a simple ASCII character

print(ord('H')) #>>72
print(ord('e')) #>>101
print(ord('\n')) #>>10
#all uppercase letters are less than lowercase letters

'Unicode'
#A universal code for hundreds of millions of different characters. Not just 128

'Multi-Byte Characters'
#To represent the wide range of characters computers must handle we represent characters with more than one byte
#   UTF-16 - Fixed length - Two bytes
#   UTF-32 - Fixed length - Four bytes
#   UTF-8 - 1-4 bytes
#       -Upwards compatible with ASCII
#       -Automatic detection between ASCII and UTF-8
#       -UTF-8 is recommended practice for encoding data to be exchanged between systems

'Byte String'
x = b'abc'
type(x) #<class 'bytes'>
x = '中文'
type(x) #<class 'str'>
x = u'中文'
type(x) #<class 'str'>

'Python 3 and Unicode'
#In Python3, all the strings internally are UNICODE
#Working with string variables in Python programs and reading data from files usually "just works"
#When we talk to a network resource using sockets or talk to a database we have to encode and decode data (usually to UTF-8)

'Python Strings to Bytes'
#When we talk to an external resource like a network socket we send bytes, so we need to encode Python3 strings into a given character encoding
#When we read data from an external resource, we must decode it based on the character set so it is properly represented in Python3 as a string

import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode() #turns it into bytes

while True:
    data = mysock.recv(512) #data is bytes
    if(len(data) < 1) :
        break
    mystring = data.decode() #assumes UTF-8 or ASCII dynamically because they are compatible with one another
    print(mystring)#this is unicode          you almost never have to tell it what it is

cmd.decode(encoding = "utf-8") #you can provide this parameter, but utf-8 is default
