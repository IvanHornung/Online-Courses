import json

data = '''{
  "name" : "Chuck",
  "phone" : {
    "type" : "intl",
    "number" : "+1 734 303 4456"
  },
  "email" : {
    "hide" : "yes"
  }
}''' #JSON represents data as nested "lists" and "dictionaries"

info = json.loads(data) #loads = load from string
print('Name:', info["name"]) #info is a dictionary! This will print "Chuck"
print('Hide:', info["email"]["hide"]) #"yes"

#JSON is not as rich as XML, but in its simplicity and relations with languages, it makes it so much easier to use

import json
input = '''[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Chuck"
  }
]''' #because it's a square bracket, it's a list. this is a list of two dictionaries

info = json.loads(input)
print('User count:', len(info))
for item in info : #this is gonna run twice
  print('Name', item['name'])
  print('Id', item['id'])
  print('Attribute', item['x'])
