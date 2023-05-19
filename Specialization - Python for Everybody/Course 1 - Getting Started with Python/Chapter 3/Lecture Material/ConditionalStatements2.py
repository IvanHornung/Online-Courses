'''else and elif'''

#else
x = 4
if x > 2:
    print('Bigger')
else :
    print('Smaller')

print('All done')

#elif & else
x = 0
if x < 2 : print('small') #one liner works
elif x < 10 :
    print('Medium')
else : 
    print('LARGE')
print('All done')

'''try & except'''
#insurance policy
istr = 'Hello Bob'
try:
    istr = int(astr)
except:
    istr = -1

print('First', istr)

astr = '123'
try:
    istr = int(astr)
except:
    istr = -1
print('Second', istr)


'''User input with try & except '''

rawstr = input('Enter a number: ')
try:
    ival = int(rawstr)
except:
    ival = -1
