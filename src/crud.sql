
INSERT INTO brand (name)
values ('BMW');

INSERT INTO brand (name)
values ('Ford');

INSERT INTO car (model, release_year, brand_id)
values ('BMW123',2000,1);

select * from brand
where id=1;

select * from car
where id=1;

update car
set model='BMW1111'
where id=1;

update brand
set name='BMW_NEW'
where id=1;

delete from car
where id=1;

delete from brand
where id=1000;



