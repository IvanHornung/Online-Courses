'Best Friends: Strings and Lists'
abc = 'With three words'
print(abc.strip())
stuff = abc.split()
print(stuff)
#>>['With', 'three', 'words']
print(len(stuff))
#>>3
print(stuff[0])
#>>With
for w in stuff :
    print(w)
#>>With
#>>Three
#>>Words

'Splitting Characteristics'
line = 'A lot                    of spaces'
etc = line.split()
print(etc)
#>>['A', 'lot', 'of', 'spaces'] #you still get 4 values no matter the whitespace

line = 'first;second;third'
thing = line.split() #standard delimiter is whitespace
print(thing)
#['first;second;third']
thing = line.split(';') #specifying the delimiter character
print(thing)
#['first', 'second', 'third']

'The Double Split Pattern'
line = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
words = line.split()
email = words[1]
pieces = email.split('@')
#['stephen.marquard', 'uct.ac.za']

#print(line.split().split('@')) this doesnt work...
