'Matching and Extracting Data'
#re.search() returns a T/F depending on whether the string matches the regular expression
#If we actually want the matching strings to be extracted, we use re.findall()

import re
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+', x) #one or more digits
print(y)
#>>['2', '19', '42']
#you get back a list from findall() of all possible matches
y = re.findall('[AEIOU]+', x)
print(y)
#>>[] no uppercase vowels

'Warning: Greedy Matching'
x = 'From: Using the : character'
y = re.findall('F.+:', x) #first character in the match is an F, one or more characters, and the last character in the match is :
print(y)
#>>['From: Using the :'] greedy matching means that you're gonna get back the larger thing

'Non-Greedy Matching'
x = 'From: Using the : character'
y = re.findall('^F.+?:', x) #first character in the match is an F, one or more characters but not greedy, last character in the match is :
print(y)
#>>['From:']

'Fine-Tuning String Extraction'
#you can refine the match for re.findall() and separately determine which portion of the match is to be extracted by using parantheses
x = 'From stephen.marquard@uct.ac.za Sat Jun  5 09:14:16 2008'
y = re.findall('\S+@\S+', x) #At least one non-whitespace character
print(y)
#>>['stephen.marquard@uct.ac.za']

#parantheses are not part of the match - but they tell where to start and stp what string to extract
y = re.findall('^From (\S+@\S+)', x) #the from is where I want to start. I demand this to match, but i only want to extract what's in parantheses
print(y)
#>>['stephen.marquard@uct.ac.za']

data = x
atpos = data.find('@')
print(atpos)
#>>21
sppos = data.find(' ',atpos) #start at atpost and look up when's the next space
print(sppos)
#>>31
host = data[atpos+1 : sppos]
print(host)
#>>uct.ac.za

'The Double Split Pattern'
line = x
words = line.split()
email = words[1]
pieces = email.split('@')
print(pieces[1])

'The Regex Version'
lin = line
y = re.findall('@([^ ]*)', lin) #look through the string until you find at @ sign. So basically like that second parameter in find
print(y) #['uct.ac.za']         also match a non-blank character([^] EVERYTHING BUT), and match many of them

'Even Cooler Regex Version'
y = re.findall('^From .*@([^ ]*)', lin) #I want a line that starts with from and a space and then any number of characters up to an @
print(y) #['uct.ac.za']                 and then I want to begin extracting all the non-blank characters and then end extracting

'Spam Confidence'
import re
hand = open('mbox-short.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line) #take 0-9 and period, one or more times
    if len(stuff) != 1 : continue
    num = float(stuff[0])
    numlist.append(num)
print('Maximum:', max(numlist)) #>>X-DSPAM-Confidence: 0.8475

'Escape Character'
#if you want a special regular expression character to just behave normally (most of the time) you prefix it with '\'
x = 'We just received $10.00 for cookies.'
y = re.findall('\$[0-9.]+', x) #a real dollar sign, one or more numbers and/or dots
print(y) #['$10.00']
