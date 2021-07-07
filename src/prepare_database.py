""" Задача 15_01.
Создать таблицу продуктов. Атрибуты продукта: id, название, цена, количество, комментарий.
Реализовать CRUD (создание, чтение, обновление по id, удаление по id) для продуктов.
Создать пользовательский интерфейс. """

# import sqlalchemy as sa
# from random import randint
# from random import choice
# from random import uniform
#
# db = sa.create_engine('sqlite:///products.db')
# db.execute('''CREATE TABLE products(
#                 id integer primary key autoincrement,
#                 name varchar,
#                 price float,
#                 count integer,
#                 comment varchar)''')
#
# db.execute('''
# insert into products('name', 'price', 'count', 'comment')
#             values ('Milk', 2.5, 300, 'BY'),
#                    ('Water', 0.5, 1000, 'BY'),
#                    ('Croissants', 3.0, 150, 'FR')
#             ''')
#
#
# name = 'Cheese Brie'
# price = 4.70
# count = 117
# comment = 'PL'
#
# db.execute(f'''
# insert into products('name', 'price', 'count', 'comment')
#             values ('{name}', '{price}', '{count}', '{comment}')
#             ''')
#
#
#
# with open('prods.txt') as fin:
#     names = fin.read()
#
# names = names.split('\n')
# comments = ['BY', 'RU', 'PL', 'FR', 'IT', 'LT', 'LV', 'ES', 'EN', 'UA']
#
# # for name in names:
# #     price = uniform(0.1, 18.7)
# #     count = randint(1, 1000)
# #     comment = choice(comments)
# #
# # db.execute(f'''
# # insert into products('name', 'price', 'count', 'comment')
# #             values ('{name}', '{price}', '{count}', '{comment}')
# #             ''')
#
# for id_ in range(5, 21):
#     price = round(uniform(0.1, 18.7), 2)
#     db.execute(f'''
#     update products
#     set price='{price}'
#     where id='{id_}'
#     ''')