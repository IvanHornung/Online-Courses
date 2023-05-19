'Geocoding-JSON'
#http://maps.googleapis.com/maps/api/geocode/json?address=Ann+Arbor%2C+MI
#                                                          +=space %2C=comma

import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True : 
  address = input('Enter Location: ')
  if len(address) < 1 : break #if we hit enter by iteself it breaks

  url = serviceurl + urllib.parse.urlencode({'address':address}) 

  print('Retrieving', url)
  uh = urllib.request.urlopen(url) #handle doesn't actually pull the data down
  data = uh.read().decode() #read() does pull the entire document, all that text. we now have python unicode string
  print('Retrieved', len(data), 'characters')

  try:
    js = json.loads(data) #parses the data that got back from Google. We get back an object: a dictionary bc JSON file is a big dict in this case
  except:
    js = None

  if not js or 'status' not in js or js['status'] != 'OK' : #so the rest of the code doesn't blow up
    print('==== Failure To Retrieve ====')
    print(data)
    continue
  
  #a dictionary that constains a list and each of those contains a dictionary...
  lat = js["results"][0]["geometry"]["location"]["lat"] #(dict: js sub results)->(list: sub 0 - the first result) and then that is a dictionary
  lng = js["results"][0]["geometry"]["location"]["lng"] #now we got geometry, location, lat/lng
  print('lat', lat, 'lng', lng)
  location = js['results'][0]['formatted_address']
  print(location)

#Google says, "Hey, you wanna use our thing. learn our syntax, write this code"
