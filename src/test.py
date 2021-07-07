from classes import SQLiteDataBase
import ui_func as ui

table = 'products'
db = SQLiteDataBase('products.db')
# db.add_item(table, name='PepsiCola', price=1.60, count=1757, comment='BY')
# db.update_item_by_id(table, 21, name="Coca-Cola", price=1.75)
print(db.get_all_columns('products'))

ai = db.get_all_items('products')
for row in ai:
    for value in row.values():
        print(value, end="  ")
    print()

print(ai[0])
#db.delete_item_by_id(table, 24)

ui.show_menu()
i = 500
print(f'{i:>5}')