''' Regular Expressions-
    Regular expressions are a language unto themselves. It's an "old school" language
    In computing , a regular expression, also referred to as "regex" or "regexp", provides
a concise and flexible means for matching strings of text, such as particular characters,
words, or patterns of characters. A regular expression is written in a formal language
that can be interpreted by a regular expression processor.
    Really clever "wild card" expressions for matching and parsing strings.

'Regular Expression Quick Guide'
^   matches the beginning of a line
$   matcges the end of the line
.   matches any character
\s  matches whitespace
\S  matches any non-whitespace character
*   repeats a character zero or more times
*?  repeats a character zero or more times (non-greedy)
+   repeats a character one or more times
+?  repeats a character one or more times (non-greedy)
[aeiou] matches a single character in the listed set
[^XYZ]  matches a single character not in the listed set
[a-z0-9]    the set of characters can include a range
(   indicates where string extraction is to start
)   indicates where string extraction is to end


--The Regular Expression Module--
    Before you can use regular expressions in your program, you must 
import the library using "import re"
    You can use re.search() to see if a string matches a regular expression,
similar to using the find() method for strings
    You can use re.findall() to extract portions of a string that match
your regular expression, similar to a combination of find() and slicing: var[5:10] '''

'Using re.search() Like find()'
#Find()
hand = open('mbox-short.txt')
for line in hand :
    line = line.rstrip()
    if line.find('From:') >= 0 :
        print(line)

#re.search()
import re
hand = open('mbox-short.txt')
for line in hand :
    line = line.rstrip()
    if re.search('From:', line) : #string we are searching for, line we that we are searching within
        print(line)


'Using re.search() Like startswith()'
#startswith()
for line in hand :
    line = line.rstrip()
    if line.startswith('From: ') :
        print(line)

#re.search()
import re
for line in hand :
    line = line.rstrip()
    if re.search('^From:', line) :
        print(line)

'Wild-Card Characters'
#the dot character matches any character
#if you add the asterisk character, the character is "any number of times"
#   ^X.*:   "I'm looking for lines that have an X in the beginning, followed by any number of characters, followed by colon"
#X-Sieve: CMU Sieve 2.3 <-- this would be matched

'Fine-Tuning Your Match'
#Depending on how "clean" your data is and the purpose of your application, you may want to narrow your match down a bit
#   ^X-\S+: "I want matches that start with X, followed by a dash, followed by any non-whitespace character=greater than
#                                       or equal to one or more non-line character, followed by a colon"
