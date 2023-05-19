'''10.2 Write a program to read through the mbox-short.txt and figure out the distribution 
by hour of the day for each of the messages. You can pull the hour out from the 'From ' line
by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.'''

fhand = open('mbox-short.txt')

hourdict = dict()
wordlst = list()
for line in fhand :
    if not line.startswith("From "): continue
    wordlst = line.split()
    timelst = wordlst[5].split(':')
    hourdict[timelst[0]] = hourdict.get(timelst[0], 0) + 1

for v, k in sorted(hourdict.items()) :
    print(v, k)
