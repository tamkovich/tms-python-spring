 CREATE TABLE car(
   id SERIAL PRIMARY KEY,
   model VARCHAR,
   release_year INT,
   brand_id INT,
   FOREIGN KEY (brand_id) REFERENCES brand(id)
   );