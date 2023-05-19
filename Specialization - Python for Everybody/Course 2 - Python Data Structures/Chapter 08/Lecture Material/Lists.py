#Algorithms - a set of rules or steps used to solve a problem
#Data Structures - a particular way of organizing data in a computer

'What is Not a "Collection"?'
x = 2
x = 4
print(x)
#>>4

'A List Is a Kind of Collection'
friends = ['Tyson', 'Glenn', 'Jaewon']
carryon = ['socks','shirt','perfume']

'List Constant'
#they do not have to be the same type of data
print(['red', 24, 98.6])
#>>['red', 24, 98.6]

#Embedded list
print([1, [5,6], 7])
#>>[1, [5,6], 7]

#empty list
print([])
#>>[]

'Lists and Definite Loops - Best Pals'
for friend in friends :
    print('Stay safe from Corona:', friend, "!")

'Looking Inside Lists'
print(friends[1])
#>>Glenn

'Lists are Mutable'
#string are immutable - you cannot change the contents of a string
#fruit = 'Banana'
#fruit = 'b'
#--Traceback error--

#lists are mutable
lotto = [2, 14, 26, 41, 63]
lotto[2] = 28
#[2, 14, 28, 41, 63]

'How Long is a List?'
greet = 'Hello Bob'
print(len(greet))
#>>9
x = [1, 2, 'joe', 99]
print(len(x))
#>>4

'Using the Range Function'
#returns a list of numbers that range from 0 to parameter-1
print(range(4))
#>>[0, 1, 2, 3]
print(range(len(friends)))
#>>[0, 1, 2]

'A Tale of Two Loops...'
for friend in friends:
    print('Sup', friend)

for i in range(len(friends)) :
    friend = friends[i]
    print('Wassup', friend)
