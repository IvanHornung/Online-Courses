#Twython Callbacks

'Using TwythonStreamer'
#First, define a new class which extends TwythonStreamer
#class MyStreamer(TwythonStreamer) :
#This allows you to redefine some of the methods of TwythonStreamer
#Define a method on_success() inside your new class
#on_success() is a callback
#   -called when a tweet is found matching your search criteria

'on_success() Callback'
class MyStreamer(TwythonStreamer) :
    def on_success(self, data):
        if 'text' in data:
            print("Found it.")
#data is a dictionary pass to on_success()
#text field of data is the matching tweet
