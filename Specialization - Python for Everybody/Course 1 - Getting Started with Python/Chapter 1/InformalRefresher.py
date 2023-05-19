##This lesson was meant to demonstrate different situations of code-reading the python engine does, but
##serves mainly to remind me of the forgotten Python content after using Java for so long.

'''
This is a multi-line comment!
'''

# You begin writing comments with a hastag

#Doesn't look like you need a class declaration or main method for now

x = 5 # you do not end a line with a semicolon
if x < 10: #if statement consists of no parameters and ends with a colon
    #there are no opening/closing brackets, so indentation is very important in python
    print('Smaller') #print statement is just "print()" with single quote string parameters
if x > 20:
    print("Bigger") # or you can use double quotes...?

print('Finished!')

n = 5
while n > 0 :
    print(n)
    n -=1 # same shortcut as in java
print('Blastoff!')
