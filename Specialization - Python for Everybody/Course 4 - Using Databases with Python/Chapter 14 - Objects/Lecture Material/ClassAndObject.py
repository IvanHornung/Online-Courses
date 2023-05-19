class PartyAnimal: #This is the template for making PartyAnimal objects
    x = 0 #Each PartyAnimal object has a bit of data.

    def party(self) : #self is convention
        self.x = self.x + 1
        print("So far". self.x)

an = PartyAnimal() #Construct a PartyAnimal object and store in a variable

an.party()
an.party() #this syntax is like a contraction for this: PartyAnimal.party(an)
an.party()

'Playing with dir() and type()'
#The dir() command lists capabilites
#The rest are real operations that the object can perform
#It is like type() - it tells us something *about* a variable

#We can use dir() to find the "capabilites" of our newly created class.
print("Type", type(an)) #>>Type <class '__main__.PartyAnimal'>
print("Dir", dir(an)) #>>Dir ['__class___', ... 'party', 'x']
