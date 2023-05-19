'''5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
Once 'done' is entered, print out the largest and smallest of the numbers. 
If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number.
Enter 7, 2, bob, 10, and 4 and match the output below.'''

smallest = 9999
largest = -9999

while True:
    inp = input("Enter numbers:\t")
    if inp == "done": break
    try:
        inp = int(inp)
    except:
        print("Invalid input")
        continue
    if inp < smallest :
        smallest = inp
    if inp > largest :
        largest = inp
print('Maximum is',largest, "\nMinimum is", smallest)
