# Homework 16
### Files description:
* `database_creation.txt` - contain a sequence of commands to create the database
* `brands.csv` - "brands" table exported from database to .cs3. **cars.csv** - "cars" table exported from database to .csv
* `hw_16_db.svg` - graphical database scheme with constrains between tables
* `select_all_clear.csv` - the result of Query #1 exported to .csv
* `select_year_2021.csv` - the result of Query #2 exported to .csv
<br><br>
```
-- Query #1
SELECT b.name, c.model, c.release_year
    FROM brands b JOIN cars c ON b.brand_id = c.brand
```


```
-- Query #2
SELECT brands.name, cars.model, cars.release_year
    FROM brands JOIN cars ON brands.brand_id = cars.brand
    WHERE cars.release_year=2021
```