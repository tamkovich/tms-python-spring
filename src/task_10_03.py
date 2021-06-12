""" Задание 10.03
Дан файл, содержащий различные даты. Каждая дата - это число, месяц и
год. Найти самую раннюю дату. [02-8.1-ML-29]
"""

import csv
from datetime import date

datas = []
with open("datas.csv", "r") as fin:
    f_reader = csv.reader(fin, delimiter=",")
    for row in f_reader:
        datas.append(row)
del(datas[0])

for index, row in enumerate(datas):
    datas[index] = list(map(int, row))

datas = map(lambda data: date(*data[::-1]), datas)

earliest_date = next(datas)
for day in datas:
    if day < earliest_date:
        earliest_date = day

print(f"The earliest date is {earliest_date}")
