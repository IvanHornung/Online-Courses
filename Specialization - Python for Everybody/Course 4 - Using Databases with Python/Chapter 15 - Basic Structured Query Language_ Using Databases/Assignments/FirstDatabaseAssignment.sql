CREATE TABLE Ages (
	name VARCHAR(128),
	age INTEGER
);

DELETE FROM Ages;
INSERT INTO Ages (name, age) VALUES ('Kehinde', 19);
INSERT INTO Ages (name, age) VALUES ('Rosheen', 30);
INSERT INTO Ages (name, age) VALUES ('Jaz', 39);
INSERT INTO Ages (name, age) VALUES ('Ismail', 21);
INSERT INTO Ages (name, age) VALUES ('Lauri', 21);

SELECT hex(name || age) AS X FROM Ages ORDER BY X;
