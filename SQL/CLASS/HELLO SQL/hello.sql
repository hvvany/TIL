-- SQLite
CREATE TABLE classmates (
id INTEGER PRIMARY KEY,
name TEXT
);

INSERT INTO classmates (id, name) VALUES (1,'홍길동');


CREATE TABLE classmates (
name TEXT,
age INT,
address TEXT
);

DROP TABLE classmates;

INSERT INTO classmates (name, age) VALUES ('홍길동', 23);

INSERT INTO classmates VALUES ('홍길동', 30, '서울');

SELECT * FROM classmates;

DROP TABLE classmates;