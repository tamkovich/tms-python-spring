"""Задание 10.00
В настоящем задании производится формирование файлов с исходными данными
для выполнения заданий 10.1 - 10.3
"""


import csv
from datetime import datetime
from datetime import timedelta
from faker import Faker
from random import randint


""" Подготовка исходных для задания 10.01
Создается файл 'data_01.csv' со случайными данными следующей структуры:
Имя, Фамилия, Возраст.
Записей в файле - 300.
"""

fake = Faker()
data = [["Firstname", "Lastname", "Age"]]
for _ in range(0, 300):
    data.append([fake.first_name(), fake.last_name(), randint(1, 122)])

with open("data_01.csv", "w") as fout:
    f_writer = csv.writer(fout, delimiter=",", lineterminator="\n")
    f_writer.writerows(data)


""" Подготовка исходных для задания 10.02
Создается файл 'data_weather.csv' с данными о ежедневной погоде
за последние days_cnt дней от текущего дня.
Структура: Дата, Место, Градусы, Скорость ветра.
Данные генерируются для пяти городов, в числе которых Минск и четыре случайных города
"""

fake = Faker()
data = [["Date", "City", "Temperature", "Wind speed"]]
cities = ["Minsk"]
today = datetime.today()
days_cnt = 31

for _ in range(4):
    cities.append(fake.city())

for day in range(days_cnt):
    day_ = today - timedelta(days=day)
    for city in cities:
        data.append([day_.strftime('%Y-%m-%d'), city, randint(9, 22), randint(0, 15)])

with open("data_weather.csv", "w") as fout:
    f_writer = csv.writer(fout, delimiter=",", lineterminator="\n")
    f_writer.writerows(data)


""" Подготовка исходных для задания 10.03
Создается файл 'datas.csv', содержащий случайные даты.
Каждая дата - это число, месяц и год.
Количество записей - 300
"""

fake = Faker()
datas = [["Day", "Month", "Year"]]
items_cnt = 300

for _ in range(items_cnt):
    datas.append(fake.date().split("-")[::-1])

with open("datas.csv", "w") as fout:
    f_writer = csv.writer(fout, delimiter=",", lineterminator="\n")
    f_writer.writerows(datas)
