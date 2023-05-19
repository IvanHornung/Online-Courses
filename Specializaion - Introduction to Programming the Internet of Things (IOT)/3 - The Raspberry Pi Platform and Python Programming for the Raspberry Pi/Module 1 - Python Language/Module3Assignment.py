'''
Write a Python program that prompts the user to input 3 numbers, one at a time. 
The Python program should put the numbers in a list, sort the list, and print the sorted list. 
Executing the program should produce results something like this:
Enter a number:
5
Enter a number:
4
Enter a number:
3
3, 4, 5
>>>
Turn in your source code and a screenshot showing a full execution of your program and 
the result that it prints to the screen. In the execution that you take a screenshot of,
you should enter the numbers in non-sorted order so that we can tell that sorting did occur.
'''

inputList = list()
for i in range(0,3) :
    inputList.append(int(input("Enter a number:")))
inputList.sort()
print(inputList)
