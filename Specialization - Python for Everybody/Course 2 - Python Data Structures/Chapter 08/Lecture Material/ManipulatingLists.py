'Concatenating Lists using +'
a = [1, 2. 3]
b = [4, 5, 6]
c = a + b
print(c)
#>>[1, 2. 3, 4, 5, 6]

'Lists Can Be Sliced Using :'
t = [9, 41, 12, 3, 74, 15]
t[1:3]
#[41,12]
t[:4]
#[9, 41, 12, 3]
t[3:]
#[3, 74, 15]
t[:]
#[9, 41, 12, 3, 74, 15]
#very much similar to a string

'Building a List from Scratch'
stuff = list() #assigns stuff into being a new, empty list 
stuff.append('book') #adds this to the list using append method
stuff.append(99)
print(stuff)
#['book', 99]
stuff.append('cookie')
print(stuff)
#['book', 99, 'cookie']

'Is Somethign in a List?'
some = [1, 9, 21, 10, 16]
9 in some
#True
15 in some
#False
20 not in some
#True

'Lists are in Order'
friends = ['Joseph', 'Glenn', 'Sally']
friends.sort()
print(friends)
#>>['Glenn', 'Joseph', 'Sally']
print(friends[1])
#>>Joseph

'Built-in Functions and Lists'
nums = [3, 41, 12, 9, 74, 15]
print(len(nums))
#>>6
print(max(nums))
#>>74
print(min(nums))
#>>3
print(sum(nums))
#>>154
print(sum(nums)/len(nums))
#>>25.6

'Calculating Average Using a List/Data Structure'
numlist = list()
while True :
    inp = input('Enter a number: ')
    if inp == 'done' : break
    value = float(inp)
    numlist.append(value)

average = sum(numlist) / len(numlist)
print('Average:', average)
