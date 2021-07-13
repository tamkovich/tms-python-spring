from sqlalchemy import create_engine

e = create_engine("sqlite:///test.db")
e.execute("""
create table products (
id integer primary key autoincrement,
name varchar, 
price float,
count integer,
comment varchar
)
""")