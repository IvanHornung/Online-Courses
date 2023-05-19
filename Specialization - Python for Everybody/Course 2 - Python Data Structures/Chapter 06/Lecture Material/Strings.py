'''Looking Inside Strings'''
fruit = 'banana'
letter = fruit[1]
print(letter)
#>>a
x = 3
w = fruit[x - 1]
print(w)
#>>n

'''len function'''
print(len(fruit))
#>>6

'''Looping Through Strings'''
index = 0
while index < len(fruit) :
    letter = fruit[index]
    print(index, letter)
    index += 1

'''For Looping Through Strings'''
for letter in fruit:
    print(letter)

'''Slicing Strings'''
s = "Monty Python"
print( s[0:4] )
#>>Mont
print( s[6:7] )
#>>P
print( s[6:20] ) #doesn't actually create a traceback if you go over the string length
#>>Python
