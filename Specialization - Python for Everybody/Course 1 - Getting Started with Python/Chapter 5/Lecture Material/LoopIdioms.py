'Counting in a Loop'
count = 0
print('Before', count)
for thing in [9, 41, 12, 3, 74, 15] :
    count += 1
    print(count, thing)
print('After', count)

'Summing in a Loop'
sum = 0
for thing in [9, 41, 12, 3, 74, 15] :
    sum += thing
    print(sum, thing)
print('Final sum:', sum)

'Finding the Average in a Loop'
count = 0
sum = 0
for value in [9, 41, 12, 3, 74, 15] :
    count += 1
    sum += value
    print(count, sum, value)
print('After', count, sum, sum/count)

'Searching Using a Boolean Variable'
found = False
for value in [9, 41, 12, 3, 74, 15] :
    if value == 3 :
        found = True
        break
    print(found, value)
print('After', found)

'How to Find the Smallest Value'
smallest_so_far = 9999
for the_num in [9, 41, 12, 3, 74, 15] :
    if the_num < smallest_so_far:
        smallest_so_far = the_num
    print(smallest_so_far, the_num)

print('After', smallest_so_far)

'How to Find the Smallest Value using None'
smallest = None
for value in [9, 41, 12, 3, 74, 15] :
    if smallest is None :
        smallest = value
    elif value < smallest :
        smallest = value
    print(smallest, value)
print('After', smallest)

if smallest is not None:
    print("is / is not => operators")

