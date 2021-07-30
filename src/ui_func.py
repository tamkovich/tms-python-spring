from classes import SQLiteDataBase


def show_menu():
    print(f"\n{'-' * 30}")
    for row in MENU:
        print(row)


def get_user_choice():
    CHOICE = ("0", "1", "2", "3", "4", "5", "6")
    while True:
        choice = input("Your choice: ")
        if choice in CHOICE:
            return choice
        else:
            print("Incorrect choice. Try again, please.\n")


def view_all_items(db: 'SQLiteDataBase', table: str):
    items = db.get_all_items(table)
    columns = db.get_all_columns(table)
    print(f"\nDATABASE ITEMS:\n{'-' * 30}")
    for column in columns:
        print(f'{column}  ', end='')
    print(f"\n{'-' * 30}", end='')
    for item in items:
        print()
        for column in item.values():
            print(column, end="  ")


def view_columns_names(db: 'SQLiteDataBase', table: str):
    columns = db.get_all_columns(table)
    print('\nCOLUMNS NAMES:')
    print(f"{'-' * 30}")
    for column in columns:
        print(f'{column}  ')


def view_item_by_id(db: 'SQLiteDataBase', table: str):
    item_id = int(input('Enter item id: '))
    columns = db.get_all_columns(table)
    item = db.get_item_by_id(table, item_id)
    print()
    for index, column in enumerate(columns):
        print(f'{column}: {item[index]}')


def add_item(db: 'SQLiteDataBase', table: str):
    columns = db.get_all_columns(table)[1:]
    print('To add item enter next attributes: ')
    item_attributes = {}
    for column in columns:
        item_attributes[column] = input(f'{column}: ')

    for attr in item_attributes:
        if item_attributes[attr].isdigit():
            item_attributes[attr] = int(item_attributes[attr])
        elif item_attributes[attr].replace(".", "", 1).isdigit():
            round(float(item_attributes[attr]), 2)

    db.add_item(table, **item_attributes)


def update_item_by_id(db: 'SQLiteDataBase', table: str):
    columns = db.get_all_columns(table)[1:]
    print('To update item enter next attributes: ')
    item_attributes = {}
    item_id = int(input('id: '))
    for column in columns:
        item_attributes[column] = input(f'{column}: ')

    for attr in item_attributes:
        if item_attributes[attr].isdigit():
            item_attributes[attr] = int(item_attributes[attr])
        elif item_attributes[attr].replace(".", "", 1).isdigit():
            round(float(item_attributes[attr]), 2)

    db.update_item_by_id(table, item_id, **item_attributes)


def erase_item_by_id(db: 'SQLiteDataBase', table: str):
    item_id = int(input('Enter item id: '))
    db.delete_item_by_id(table, item_id)


MENU = [
    '1 - View all items',
    '2 - View columns names',
    '3 - View item by id',
    '4 - Add item',
    '5 - Update item by id',
    '6 - Erase item by id',
    '0 - Exit program'
]

ACTIONS = {
    '1': view_all_items,
    '2': view_columns_names,
    '3': view_item_by_id,
    '4': add_item,
    '5': update_item_by_id,
    '6': erase_item_by_id
}
