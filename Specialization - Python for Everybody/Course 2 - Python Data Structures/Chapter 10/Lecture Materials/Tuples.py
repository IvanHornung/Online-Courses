'Tuples Are Like Lists' #unmodifable lists...

x = ('Glenn', 'Sally', 'Joseph')
print(x[2]) #>>Joseph
y = (1, 9, 2 )
print(y) #(1, 9, 2 )
print(max(y)) #>>9

for iter in y :
    print(iter)

'but... Tuples are "immutable"'
#Unlike a list, once you create a tuple, you cannot alter its contents - similar to a string

z = (5, 4, 3)
#z[2] = 0
#Traceback Error

'A Tale of Two Sequences'
l = list()
dir(1)
#fat list
t = tuple()
dir(t)
#['count', 'index']

'Tuples and Assignment'
#we can also put tuples on the left-hand side of an assignment statement
#you can even omit the parantheses
(x, y) = (4, 'fred')
print(y) #fred
(a, b) = (99, 98)
print(a) #99

'Tuples and Dictionaries'
#The items() method in dictionaries returns a list of (key, value) tuples
d = dict()
d['csev'] = 2
d['cwen'] = 4
for (k, v) in d.items() :
    print(k, v)

tups = d.items()
print(tups) #dict_items([('csev', 2), ('cwen', 4)])

'Tuples are Comparable'
print((0, 1, 2) < (5, 1, 2)) #True
print((0, 1, 200000) < (0, 3, 4)) # True
print(('Jones', 'Sally') < ('Jones', 'Same')) #True
print(('Jones', 'Sally') > ('Adams', 'Sam')) #True

'Sorting Lists of Tuples'
d = {'a':10, 'b':1, 'c':22}
d.items()
#dict_items([('a', 10), ('c', 22), ('b', 1)])
sorted(d.items())
#[('a', 10). ('b', 1), ('c', 22)]

'Using sorted()'
d = {'a':10, 'b':1, 'c':22}
t = sorted(d.items())
#[('a', 10), ('b', 1), ('c', 22)]
for k, v in sorted(d.items()) :
    print(k, v)
'''
a 10
b 1
c 22
    '''

'Sort by Values Instead of Key'
c = {'a':10, 'b':1, 'c':22}
tmp = list()
for k, v in c.items():
    tmp.append( (v, k) )
print(tmp) #[(10, 'a'), (22, 'c'), (1, 'b')]
tmp = sorted(tmp, reverse = True) #sorts backwards
print(tmp) #[(22, 'c'), (10, 'a'), (1, 'b')]



'The 10 most common words'
fhand = open('romeo.txt')
counts = dict()
for line in fhand :
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    
lst = list()
for key, val in counts.items() :
    newtup = (val, key)
    lst.append(newtup)

lst = sorted(lst, reverse = True)

for val, key in lst[:10] :
    print(key, val)

'EVEN SHORTER VERSION. THE ONE LINER'

c = {'a':10, 'b':1, 'c':22}
print( sorted([ (v, k) for k,v in c.items() ], reverse = True))
#[(1, 'b'), (10, 'a'), (22, 'c')]
#List comprehension creates a dynamic list. In this case,
#we make a list of reversed tuples and then sort it

#TODO Search List Comprehension - creates a dynamic list. In this case, we make a list of reserved tuples and then sort it.
