from sqlalchemy import create_engine
from sqlalchemy.sql import text


def insert(name, price, count, comment):
    engine = create_engine("sqlite:///test.db")
    query = "INSERT INTO products (name, price, count, comment)  VALUES (:n, :p, :c, :comm);"
    result = engine.execute(text(query), n=name, p=price, c=count, comm=comment)
    if result:
        print("inserted")
    else:
        print("error in insert")


def read():
    engine = create_engine("sqlite:///test.db")
    query = "SELECT * FROM products;"
    result = engine.execute(text(query))
    if result:
        for i in result:
            print(f'id is: {i[0]}')
            print(f'name is: {i[1]}')
            print(f'price is: {i[2]}')
            print(f'count is: {i[3]}')
            print(f'comment is: {i[4]}')
    else:
        pass


def delete(ident):
    engine = create_engine("sqlite:///test.db")
    query = "DELETE FROM products WHERE id=:ident;"
    result = engine.execute(text(query), ident=ident)
    if result:
        print("deleted")
    else:
        print("error in delete")


def update(ident, name, price, count, comment):
    engine = create_engine("sqlite:///test.db")
    query = "UPDATE products SET name=:n, price=:p, count=:c, comment=:comm WHERE id=:ident;"
    result = engine.execute(text(query), n=name, p=price, c=count, comm=comment, ident=ident)
    if result:
        print("updated")
    else:
        print("error in update")


# insert("Samsung",300, 23,"samsung")
delete(1)
