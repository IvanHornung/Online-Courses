'Database Design'
#Database design is an art form of its own with particular skills and experience
#Our goal is to avoid the really bad mistakes and design clean and easily understood databases
#Others may performance tune things later
#Database design starts with a picture.

'Building a Data Model'
#Drawing a picture of the data objects for our application and then figuring out how to represent the objects and their relationships
#Basic Rule: Don't put the same string data in twice - use a relationship instead
#When there is one thing in the "real world" there should be one copy of that thing in the database

'For each "peice of info"...'
#Is the column an object or an attribute of another object?
#Once we define objects, we need to define the relationships between objects
''' First question. "The thing that is the most essential to this application. What is the one-sentence description of this application?"
        A thing that manages tracks. Part of a track: *; Not part of the track: -
**Track                         |Track  | belongs to
-Album                          |Rating |\______>|Album|---> |Artist|
-Artist                         |Len    |/
-Genre                          |Count  |
*Rating                             |
*Len                            |Genre  |
*Count   
'''
