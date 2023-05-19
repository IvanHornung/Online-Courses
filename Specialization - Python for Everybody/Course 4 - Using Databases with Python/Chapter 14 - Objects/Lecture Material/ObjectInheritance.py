'Inheritance'
#When we make a new class - we can reuse an existing class and inherit all the capabilites of an existing class
#       and then add our own little bit to make our new class
#Another form of store and reuse
#Write once - reuse many times
#The new class (child) has all the capabilities of the old class (parent) - and then some more

class PartyAnimal:
    x = 0
    name = ""

    def __init__(self, nam) :
        self.name = nam
        print(self.name, "constructed")

    def party(self) :
        self.x = self.x + 1
        print(self.name, "party count", self.x)

class FootballFan(PartyAnimal) : #a class which extends PartyAnimal. It has all the capabilites of PartyAnimal and more
    points = 0
    def touchdown(self) :
        self.points = self.points + 7
        self.party()
        print(self.name, "points", self.points) 
        
s = PartyAnimal("Sally")
s.party()

j = FootballFan("Jim")
j.party()
j.touchdown()
