'SQLite Browser'
#SQLite is a very popular database - it is free and fast and small
#SQLite Browser allows us to directly manipulate SQLite files
#   - http://sqlitebrowser.org/
#There is also a Firefox plugin to manipulate SQLite database
#   - https://addons.mozilla.org/en-US/firefox/addon/sqlite-manager/
#SQLite is embedded in Python and a number of other languages.

'SQL Insert'
#The insert statement inserts a row into a table
#INSERT INTO Users(name, email) VALUES('Kristin', 'kf@umich.edu')

'SQL Delete'
#Deletes a row in a table based on a selecton criteria
#DELETE FROM Users WHERE email='ted@umich.edu'

'SQL: Update'
#Allows the updating of a field with a where clause
#UPDATE Users SET name='Charles' WHERE email='csev@umich.edu'

'Retrieving Records: Select'
#The select statement retrieves a group of records - you can either retrieve
#all the records or a subset of the records with a WHERE clause

#SELECT * FROM Users
#SELECT * FROM Users WHERE email='csev@umich.edu'

'Sorting with ORDER BY'
#You can add an ORDER BY clause to SELECT statements to get the results sorted in ascending or descending order

#SELECT * FROM Users ORDER BY email
#SELECT * FROM Users ORDER BY name
