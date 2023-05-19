'Counting Pattern'
counts = dict()
line = input('')

words = line.split()

print('Words:', words)

print('Counting...')
for word in words:
    counts[word] = counts.get(word, 0) + 1
print('Counts', counts)

'Definite Loops and Dictionaries'
counts = {'chuck': 1, 'fred': 42, 'jan': 100}
for key in counts :
    print(key, counts[key]) 
'''
jan 100
chuck 1
fred 42
    '''

'Retrieving lists of Keys and Values'
jjj = {'chuck': 1, 'fred': 42, 'jan': 100}
print(list(jjj)) # ['jan', 'chuck', 'fred']
print(jjj.keys()) # ['jan', 'chuck', 'fred']
print(jjj.values()) # [100, 1, 42]
print(jjj.items()) #[('jan', 100), ('chuck', 1), ('fred', 42)]

'Bonus: Two Iteration Variables!'
for aaa, bbb in jjj.items() :
    print(aaa, bbb)
'''
jan 100
chuck 1
fred 42
    '''

'The Finale'
name = input('Enter file: ')
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    
bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)
