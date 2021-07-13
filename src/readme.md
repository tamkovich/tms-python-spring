# Homework 16
## Files description:
1. **database_creation.txt** - contain a sequence of commands to create the database
2. **brands.csv** - "brands" table exported from database to .csv
3. **cars.csv** - "cars" table exported from database to .csv
4. **hw_16_db.svg** - graphical database scheme with constrains between tables
5. **select_all_clear.csv** - the result of Query #1 exported to .csv
6. **select_year_2021.csv** - the result of Query #2 exported to .csv

<br><br>
<code>
-- Query #1 <br>
select b.name, c.model, c.release_year <br>
    from brands b join cars c on b.brand_id = c.brand
</code>
<br><br>
<code> 
-- Query #2<br>
select brands.name, cars.model, cars.release_year from
        brands join cars on brands.brand_id = cars.brand
        where cars.release_year=2021
</code>