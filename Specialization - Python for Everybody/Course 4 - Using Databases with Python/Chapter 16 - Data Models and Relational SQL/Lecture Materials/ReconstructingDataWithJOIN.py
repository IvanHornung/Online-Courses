'Relational Power'
#By removing the replicated data and replacing it with references to a single copy of each bit of data we build a "web"
#       of information that the relational database can read through very quickly - even for very large amounts of data.
#Often when you want some data it comes from a number of tables linked by these foreign keys.

'The JOIN Operation'
#The JOIN operation links across several tables as part of a select operation.
#You must tell the JOIN how to use the keys that make the connection between the tables using an ON clause. 

'Without an ON Clause'
#SELECT Track.title, Track.genre_id, Genre.id, Genre.name FROM Track JOIN Genre

#Joining two tables without an ON clause gives all possible combinations of rows.

'It can get complex...'
#select Track.title, Artist.name, Album.title, Genre.name from Track join Genre join Album join Artist on Track.genre_id = Genre.id and Track.album_id = Album.id and Album.artist_id = Artist.id
