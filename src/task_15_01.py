""" Задача 15_01.
Создать таблицу продуктов. Атрибуты продукта: id, название, цена, количество, комментарий.
Реализовать CRUD (создание, чтение, обновление по id, удаление по id) для продуктов.
Создать пользовательский интерфейс. """

from classes import SQLiteDataBase
import ui_func as ui

db = SQLiteDataBase('products.db')
table = 'products'
while True:
    ui.show_menu()
    user_choice = ui.get_user_choice()
    if user_choice == '0':
        break
    ui.ACTIONS[user_choice](db, table)

print("Exit program.")

