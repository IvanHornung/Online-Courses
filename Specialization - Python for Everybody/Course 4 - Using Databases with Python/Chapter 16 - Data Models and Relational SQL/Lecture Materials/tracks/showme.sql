SELECT Track.title, Album.title, Artist.name FROM Track
JOIN Album JOIN Artist ON Track.album_id = Album.id AND Album.artist_id  =
Artist.id;
