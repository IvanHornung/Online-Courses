#Sending a Tweet

'Sending a Tweet'
#Use the keys to create the Twython object

from twython import Twython

C_KEY = ""
C_SECRET = ""
A_TOKEN = ""
A_SECRET = ""

api = Twython(C_KEY, C_SECRET, A_TOKEN, A_SECRET)

api.update_status(status="Hi")

'Searching for a Hashtag'
#Maybe we want the Raspberry Pi to react to a hashtag
#When a hashtag appears, do something
#Need to scan the Twitter stream for the hashtag

'Twython Streamer'
#A TwythonStreamer object allows you to examine public streams
#TwythonStreamer has a method which searches for text in streams,
statuses.filter()
#Pass as an argument the terms you want to track
#i.e.
stream.statuses.filter(track='Harris')
