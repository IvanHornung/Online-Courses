import xml.etree.ElementTree as ET #syntax of as = alias. ends up being a short form so you don't have to type out the long thing

#triple quoted string: multiline string. newlines are part of the string
#emulating urllib and a read()
data = '''<person>
    <name>Chuck</name>
    <phone type="intl">
        +1 734 303 4456
    </phone>
    <email hide="yes"/>
</person>'''

tree = ET.fromstring(data) #take this string, and give us back like this tree. tree of information that is properly parsed
#this can blow up if there was a syntax error in the XML.
print('Name:', tree.find('name').text) #if you wanna get the text that's in between the tag & /tag, you say this. returns "Chuck"
print('Attr:', tree.find('email'.get('hide'))) #if you want to get the attribute, not the text node. go get me the attribute named tag within tag email
#returns "yes"



'If There Are Multiple Child Tags'

import xml.etree.ElementTree as ET
input = '''<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>'''

stuff = ET.fromstring(input) #stuff is a tree object of information that is parse and gives us methods to use with the data
lst = stuff.findall('users/user') #search for all of the user tags below users. a list of the whole tags
print('User count:', len(lst))
for item in lst:
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute', item.get("x"))
