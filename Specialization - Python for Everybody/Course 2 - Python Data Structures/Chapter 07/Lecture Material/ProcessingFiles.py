'Experimenting with substrings'
fruit = 'banana'
print(fruit[3:])
#It prints 'ana'! No need for an upperbound!

'File Handle as a Sequence'
xfile = open('mbox.txt')
for line in xfile: #treat a file hand as a sequence of lines
    print(line)

'Counting Lines in a File'
xfile = open('mbox.txt')
count = 0
for line in fhand:
    count += 1
print('Line Count:', count)

'Reading the *Whole* File'
fhand = open('mbox-short.txt')
inp = fhand.read()
print(len(inp))
#>>94626
print(inp[:20]) #begining up to the number before 20
#>>From stephen.marquar

'Searching Through a File'
for line in fhand:
    if line.startswith('From:') :
        print(line)

'''output
will look like
this. Why all the blank lines?'''

#This is because the print function adds a newline on top of the file's!

'Searching Through a File (fixed)'
for line in fhand:
    line = line.rstrip() #strip the whitespace on the right-hand side of the string
    if line.startswith('From:') :
        print(line)

'Skipping with Continue'
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From:'):
        continue
    print(line)

"Using 'in' tp Select lines"
for line in fhand:
    line = line.rstrip()
    if not '@uct.ac.za' in line:
        continue
    print(line)

'Prompt for File Name'
fname = input('Enter the file name:\t')
fhand = open(fname)
count = 0
for line in fhand :
    if line.startswith('Subject:') :
        count += 1
print('There were', count, 'subject lines in ', fname)


'Bad File Names'
fname = input('Enter the file name:\t')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:',fname)
    quit()
count = 0
for line in fhand :
    if line.startswith('Subject:') :
        count += 1
print('There were', count, 'subject lines in ', fname)
