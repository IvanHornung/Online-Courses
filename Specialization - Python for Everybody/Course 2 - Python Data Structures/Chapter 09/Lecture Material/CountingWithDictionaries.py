'Many Counters with a Dictionary'
ccc = dict()
ccc['csev'] = 1
ccc['cwen'] = 1
print(ccc) #{'csev': 1, 'cwen': 1}
ccc['cwen'] += 1
print(ccc) #{'csev': 1, 'cwen': 2}

'When We See a New Name'
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names :
    if name not in counts :
        count[name] = 1
    else :
        counts[name] += 1
print(counts)
#histogram-like

'The get Method for Dictionaries'
if name in counts:
    x = counts[name]
else :
    x = 0
'''
The pattern of checking to see if a key is already in a dictionary and assuming
a default value if the key is not there is so common that there is a method 
called get() that does this for us
'''
x = counts.get(name, 0) # key, default

'Simplified Counting with get()'
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names :
    counts[name] = counts.get(name,0) + 1
print(counts)
