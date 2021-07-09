# Создать таблицу продуктов.
# Атрибуты продукта: id, название, цена, количество,
# комментарий. Реализовать CRUD(создание, чтение,
# обновление по id, удаление по id) для продуктов.
# Создать пользовательский интерфейс.

import sqlite3

connection = sqlite3.connect("HW_15.db")

cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS tab_products (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                           col_name TEXT,
                                                           col_price INTEGER,
                                                           col_quantity INTEGER,
                                                           col_comment TEXT)''')


def add_position():
    name = input('введите название товара...')
    price = float(input('введите цену...'))
    quantity = int(input('введите количество...'))
    comment = input('введите комментарий...')
    cursor.execute('''INSERT INTO tab_products
                   (col_name, col_price, col_quantity, col_comment)
                   VALUES (?, ?, ?, ?)''', (name, price, quantity, comment))
    connection.commit()


def read_table():
    cursor.execute('''SELECT * FROM tab_products''')
    k = cursor.fetchall()
    for i in k:
        s = ''
        for j in i:
            s += str(j) + ' '
        print(s)


def update_table():
    iden = int(input('введите позицию чтобы поменять...'))
    name = input('введите название товара...')
    price = input('введите цену...')
    quantity = input('введите количество...')
    comment = input('введите комментарий...')
    if name:
        cursor.execute('''UPDATE tab_products SET
                   col_name=? WHERE id=?
                   ''', (name, iden))
    if price:
        price = float(price)
        cursor.execute('''UPDATE tab_products
                   SET col_price=? WHERE id=?
                   ''', (price, iden))
    if quantity:
        quantity = int(quantity)
        cursor.execute('''UPDATE tab_products
                   SET col_quantity=? WHERE id=?
                   ''', (quantity, iden))
    if comment:
        cursor.execute('''UPDATE tab_products
                   SET col_comment=? WHERE id=?
                   ''', (comment, iden))
    connection.commit()


def delete_position(iden):
    cursor.execute('''DELETE FROM tab_products WHERE id=?''', (iden,))
    connection.commit()


# add_position()
# delete_position(2)
# update_table()
# read_table()
# update_table()
# read_table()
