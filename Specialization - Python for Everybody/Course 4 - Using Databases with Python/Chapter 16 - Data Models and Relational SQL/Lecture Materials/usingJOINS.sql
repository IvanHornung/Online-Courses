select Album.title, Artist.name from Album join Artist on Album.artist_id = Artist.id;
--   what we want to see     the tables that hold the data    how the tables are linked

select Album.title, Album.artist_id, Artist.id, Artist.name from Album join Artist on Album.artist_id = Artist.id;

select Track.title, Genre.name from Track join Genre on Track.genre_id = Genre.id;

SELECT Track.title,
	Track.genre_id, 
	Genre.id, Genre.name 
FROM Track JOIN Genre;

select Track.title, Artist.name, Album.title, Genre.name from
Track join Genre join Album join Artist on Track.genre_id = 
Genre.id and Track.album_id = Album.id and Album.artist_id =
Artist.id
