'A Story of Two Collections...'
#List - A linear collection of values that stay in order
#Dictionary - A "bag" of values, each with its own label
'''
Dictionaries are Python's most powerful data collection
Dictionaries allow us to do fast database-like operations in Python
Dictionaries have different names in different languages
 -Associative Array - Perl / PHP
 -Properties or Map or HashMap - Java
 -Property Bag - C# / .Net
'''

'Dictionaries'
purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
print(purse)
#>>{'money': 12, 'tissues': 75. 'candy': 3}
print(purse['candy'])
#>>3
purse['candy'] = purse['candy'] + 2 #are mutable
print(purse)
#>>{'money': 12, 'tissues': 75. 'candy': 5}

'Comparing Lists and Dictionaries'
#declaration
lst = list()
ddd = dict()

#adding
lst.append(21)
ddd['age'] = 21
lst.append(183)
ddd['course'] = 182

print(lst) #[21, 183]
print(ddd) #{'course': 182, 'age': 21} Don't expect the order of dictionaries to be a predictable thing

lst[0] = 23
ddd['age'] = 23

print(lst) #[23, 183]
print(ddd) #{'course': 182, 'age': 23}

'Dictionary Literals (Constants)'
jjj = { 'chuck': 1, 'fred': 42, 'jan': 100}
print(jjj) #{ 'chuck': 1, 'fred': 42, 'jan': 100}
ooo = { }
print(ooo) #{}
