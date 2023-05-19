insert into Artist (name) values ('Led Zepplin');
insert into Artist (name) values ('AC/DC');

insert into Genre (name) values ('Rock');
insert into Genre (name) values ('Metal');

insert into Album (title, artist_id) values ('Who Made Who', 2);
insert into Album (title, artist_id) values ('IV', 1);

insert into Track (title, rating, len, count, album_id, genre_id) values ('Black Dog', 5, 297, 0, 2, 1);
insert into Track (title, rating, len, count, album_id, genre_id) values ('Stairway', 5, 482, 0, 2, 1);
insert into Track (title, rating, len, count, album_id, genre_id) values ('About to Rock', 5, 313, 0, 1, 2);
insert into Track (title, rating, len, count, album_id, genre_id) values ('Who Made Who', 5, 207, 0, 1, 2);
