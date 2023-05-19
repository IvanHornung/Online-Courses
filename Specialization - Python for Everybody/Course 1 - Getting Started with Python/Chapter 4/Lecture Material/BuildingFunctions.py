'''Building functions'''

x = 5
print('Hello')

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')

print('Yo')
print_lyrics()
x = x + 2
print(x)

'''OP:
Hello
Yo
I'm a lumberjack, and I'm okay.
I sleep all night and I work all day.
7'''

def greet(lang):
    if lang == 'es':
        print('Hola')
    elif lang == 'fr':
        print("Bonour")
    else:
        print('Hello')

greet('fr')
#>>>Bonjour

'''return statements'''

def sayHello():
    return "Hello"

print(sayHello(), "Glenn")
#>>Hello Glenn
print(greet('es'), 'Jaewon')
#>>Hola Jaewon

'''multiple parameters'''

def addtwo(a, b) :
    added = a + b
    return added

x = addtwo(3,5)
print(x)
#>>8
