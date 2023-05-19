'String Concatenation'
a = 'Hello'
b = a + 'There'
print(b)
#>>HelloThere
c = a + ' ' + 'There'
print(c)
#>>Hello There

'Using in as a Logical Operator'
fruit = 'banana'
'n' in fruit
#>>True
'm' in fruit
#>>False
if 'a' in fruit :
    print('Found it!')
#>> Found it!

'String Comparison'
word = 'compsci'
if word < 'banana': #A < a; z < a
    print('Your word', + word + ', comes before banana.')
elif word > 'banana':
    print('Your word', + word + ', comes after banana.')
else: print('All right, bananas.')

'String Library' #built-in functions
greet = 'Hello Bob'
zap = greet.lower()
print(zap)
#>>hello bob
print('Hi There'.lower())
#>>hi there

'Dir command'
stuff = 'Hello world'
dir(stuff) 
#prints out all the methods you can call on built-in the string class

'Searching a String'
fruit = 'banana'
pos = fruit.find('na')
print(pos)
#>>2
aa = fruit.find('z')
print(aa)
#>>-1

'Making Everything UPPER CASE'
greet = 'Hello Bob'
nnn = greet.upper()
print(nnn)
#>>HELLO BOB
www = greet.lower()
print(www)
#>>hello bob

'Search and Replace'
greet = 'Hello Bob'
nstr = greet.replace('Bob','Jane')
print(nstr)
#>>Hello Jane
nstr = greet.replace('o','X')
print(nstr)
#>>HellX BXb

'Stripping Whitespace'
greet = '      Hello Bob  '
greet.lstrip()
#'Hello Bob  '
greet.rstrip()
#'    Hello Bob'
greet.strip()
#'Hello Bob'

'Prefixes'
line = 'Please have a nice day'
line.startswith('Please')
#True
line.startswith('p')
#False

'Parsing and Extracting'
data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
atpos = data.find('@')
print(atpos)
#>>21
sppos = data.find(' ', atpos) #second parameter: where to start
print(sppos)
#>>31
host = data[atpos+1 : sppos]
print(host)
#>>uct.ac.za
