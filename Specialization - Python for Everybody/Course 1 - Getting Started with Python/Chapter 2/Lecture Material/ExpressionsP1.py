
print(float(9) ** 2) #casting syntax, as well as power syntax

i = 42 
type(i) #built in function tells you what type the variable is
#Output: <class'int'>

#Integer division produces a floating point result

print( 10 / 2 )
#OP: 5.0

'''String Conversions'''

sval = '123'
type(sval)
#<class 'str'>
ival = int(sval)
type (ival)
# <class 'int'>
print(ival+1)
# 124
nsv = 'hello bob'
#niv = int(nsv)
'''error'''

'''User input'''

name = input('Who are you') #prompt; prints out this and waits
print('Welcome', name) #comma puts a space between the two
print('NoSpace' + name)
