'''Optional: Just for Fun
There are a number of different ways to approach this problem. While we don't recommend trying to write the most compact code possible, it can sometimes be a fun exercise. Here is a a redacted version of two-line version of this program using list comprehension:

Python 2
import re
print sum( [ ****** *** * in **********('[0-9]+',**************************.read()) ] )

Python 3:
import re
print( sum( [ ****** *** * in **********('[0-9]+',**************************.read()) ] ) )
Please don't waste a lot of time trying to figure out the shortest solution until you have completed the homework. List comprehension is mentioned in Chapter 10 and the read() method is covered in Chapter 7.'''

import re
print(sum([int(i) for i in re.findall('[0-9]+', open("regexassignment.txt").read())]))
