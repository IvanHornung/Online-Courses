'''Loops'''

n = 5
while n > 0 :
    print(n)
    n -= 1
print('Blastoff!')
print(n)
'''OP
5
4
3
2
1
Blastoff!
0'''

'''Break''' #stops all iteration in the loop and continues to the following code
while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('Done!')

'''Continue''' #abandons current iteration and goes to the next
while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')
