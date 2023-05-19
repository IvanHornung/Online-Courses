'Many to Many'
#Sometimes we need to model a relationship that is many-to-many
#We need to add a "connection" table with two foreign keys
#There is usually no separate primary key
'''
_______      _________
|     |\    /|       |
|Books|------|Authors|
|     |/    \|       |

TURNS INTO
_______     _________Author-Book Junction Table
|Books|----*|Authors|     _________
            | Books |*----|Authors|
''' ''' 
Course          User
|title|<------>|name |
     many     m|email|

Course      Member  m     o User
id <----| m user_id ------->id
title o |---course_id       name
                            email

'''
