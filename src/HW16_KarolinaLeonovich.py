# Создать таблицы Brand(name),
# Car(model, release_year, brand (foreign key на таблицу Brand)).
# Реализовать CRUD(создание, чтение, обновление по id, удаление по id)
# для бренда и машины. Создать пользовательский интерфейс.


import csv
import sqlite3


connection = sqlite3.connect("HW_16.db")

cursor = connection.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS brand (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                           col_brand TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS car (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                           col_model TEXT,
                                                           col_release_year INTEGER,
                                                           col_car_brand TEXT,
                                                           FOREIGN KEY(col_car_brand)
                                                           REFERENCES brand(col_brand))''')

# Записываем в таблицу brand брэнды из
# какого-то скаченого csv из интернета


with open('csv.csv', newline='') as file:
    reader = csv.reader(file, delimiter=";")
    list_brands = []
    for row in reader:
        if row[0] not in list_brands:
            list_brands.append(row[0])
            cursor.execute('''INSERT INTO brand
                           (col_brand)
                           VALUES (?)''', (row[0],))
            connection.commit()

# прочитать все брэнды

cursor.execute('''SELECT * FROM brand''')
k = cursor.fetchall()
for i in k:
    s = ''
    for j in i:
        s += str(j) + ' '
    print(s)

# тут записываем таблицу с машинами. Небольшой гемор
# изза структуры сиэсви файла

with open('csv.csv', newline='') as file:
    reader = csv.reader(file, delimiter=";")
    for row in reader:
        if row[3] == "-":
            cursor.execute('''SELECT * FROM brand''')
            k = cursor.fetchall()
            for position in k:
                if position[1] == row[0]:
                    cursor.execute('''INSERT INTO car
                                   (col_model, col_release_year, col_car_brand)
                                   VALUES (?, ?, ?)''', (row[1], int(row[2]), position[0]))
                    connection.commit()
        else:
            cursor.execute('''SELECT * FROM brand''')
            k = cursor.fetchall()
            for position in k:
                if position[1] == row[0]:
                    cursor.execute('''INSERT INTO car
                                   (col_model, col_release_year, col_car_brand)
                                   VALUES (?, ?, ?)''', (row[1], int(row[2]), position[0]))
                    connection.commit()
            cursor.execute('''SELECT * FROM brand''')
            k = cursor.fetchall()
            for position in k:
                if position[1] == row[0]:
                    cursor.execute('''INSERT INTO car
                                   (col_model, col_release_year, col_car_brand)
                                   VALUES (?, ?, ?)''', (row[1], int(row[3]), position[0]))
                    connection.commit()

# прочитать все из машин

cursor.execute('''SELECT * FROM car''')
k = cursor.fetchall()
for i in k:
    s = ''
    for j in i:
        s += str(j) + ' '
    print(s)

# круд делать не буду потому что уже делала
