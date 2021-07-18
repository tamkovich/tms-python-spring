/*CREATE TABLE brand(
    id serial PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE car(
    id serial PRIMARY KEY,
    model VARCHAR(50),
    release_year INTEGER,
    brand_id  INTEGER,
    FOREIGN KEY (brand_id) REFERENCES brand(id)
);

INSERT INTO brand (name)
    VALUES ('mersedes'), ('audi'), ('bmw'), ('tesla');

INSERT INTO car (model, release_year, brand_id)
    VALUES  ('s500', 2010, 1),
            ('rs6', 2005, 2),
            ('m5', 2000, 3),
            ('modelS', 2017, 4),
            ('s8', 2013, 2);


INSERT INTO brand (name)
    VALUES ('bugati');

INSERT INTO car (model, release_year, brand_id)
    VALUES  ('veron', 2006, NULL);


DELETE FROM brand
WHERE id BETWEEN 5 and 9;
DELETE FROM car
WHERE id BETWEEN 6 and 10;

*/
/*Покаать обе таблицы */
SELECT * FROM brand;
SELECT * FROM car;


/**/
SELECT B.name as brand, model, release_year
FROM car C
INNER JOIN brand B ON
C.brand_id = B.id ;


SELECT B.name as brand, model, release_year
FROM car C
LEFT JOIN brand B ON
C.brand_id = B.id 
WHERE B.id IS NULL;

SELECT B.name as brand, model, release_year
FROM car C
LEFT JOIN brand B ON
C.brand_id = B.id ;

SELECT B.name as brand, model, release_year
FROM car C
RIGHT JOIN brand B ON
C.brand_id = B.id 
WHERE C.brand_id IS NULL;

SELECT B.name as brand, model, release_year
FROM car C
RIGHT JOIN brand B ON
C.brand_id = B.id ;

SELECT B.name as brand, model, release_year
FROM car C
FULL OUTER JOIN brand B ON
C.brand_id = B.id 
WHERE C.brand_id IS NULL OR B.id IS NUll;

SELECT B.name as brand, model, release_year
FROM car C
FULL OUTER JOIN brand B ON
C.brand_id = B.id ;