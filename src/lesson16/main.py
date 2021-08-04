from sqlalchemy import create_engine

engine = create_engine("sqlite:///test.db")

engine.execute(
    """
    create table user (
        id integer primary key autoincrement, firstname varchar,
        lastname varchar
    ) 
    """
)

engine.execute(
    "insert into user (firstname, lastname) values (:firstname, :lastname)",
    firstname="Pasha", lastname='Ivanov'
)
