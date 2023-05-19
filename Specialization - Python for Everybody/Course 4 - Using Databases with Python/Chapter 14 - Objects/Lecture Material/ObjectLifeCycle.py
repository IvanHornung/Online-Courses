'Object Lifecycle'
#Objects are created, used, and discarded
#We have special block of code (methods) that get called
#   -At the moment of creation (constructor)
#   -At the moment of destruction (destructor)
#Constructors are used a lot
#Destructors are seldom used

'Constructor'
#The primary purpose of the constructor is to set up some instance variables to have the proper initial vlaues when the object is created.

class PartyAnimal:
    x = 0

    def __init__(self) :
        print('I am constructed')

    def party(self) :
        self.x = self.x + 1
        print('So far', self.x)
    
    def __del__(self) :
        print('I am destructed', self.x)

an = PartyAnimal()
an.party()
an.party()
an = 42
print('an contains', an)

'Constructor'
#In object oriented programming, a constructor in a class is a special block of statements called when an object is created

'Many Instances'
#We can create lots of objects - the class is the template for the object
#We can store each distinct object in its own variable
#We call this having multipel instances of the same class
#Each instance has its own copy of the instance variables

class PartyAnimal:
    x = 0
    name = ""

    def __init__(self, z) :
        self.name = z
        print(self.name, "constructed")

    def party(self) :
        self.x = self.x + 1
        print(self.name, "party count", self.x)

s = PartyAnimal("Sally")
s.party()

j = PartyAnimal("Jim")
j.party()
s.party()
