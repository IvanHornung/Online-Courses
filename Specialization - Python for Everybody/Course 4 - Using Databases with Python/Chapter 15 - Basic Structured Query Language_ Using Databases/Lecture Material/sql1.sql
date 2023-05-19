CREATE TABLE Users ( --create table named users
	name VARCHAR(128), --field, type of field
	email VARCHAR(128) --up to 128 characters
)
INSERT INTO Users(name, email) VALUES('Kristin', 'kf@umich.edu')

DELETE FROM Users WHERE email='ted@umich.edu'

UPDATE Users SET name='Charles' WHERE email='csev@umich.edu'

SELECT * FROM Users --SELECT takes a list of columns and * means all the columns FROM is a keyword & Users is the database
SELECT * FROM Users WHERE email='csev@umich.edu'

SELECT * FROM Users ORDER BY email
SELECT * FROM Users ORDER BY name
