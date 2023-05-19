'''9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number
of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the 
person who sent the mail. The program creates a Python dictionary that maps the sender's mail address 
to a count of the number of times they appear in the file. After the dictionary is produced, the program 
reads through the dictionary using a maximum loop to find the most prolific committer.'''

handle = open('mbox-short.txt')

wordict = dict()
for line in handle :
    if not line.startswith("From "): continue
    words = line.split()
    wordict[words[1]] = wordict.get(words[1], 0) + 1


proEmail = None
proCount = None
for key, value in wordict.items() :
    if proCount is None or value > proCount :
        proEmail = key
        proCount = value

print(proEmail, proCount)
