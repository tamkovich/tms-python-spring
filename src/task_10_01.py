""" Задание 10.01
Создать csv файл с данными следующей структуры: Имя, Фамилия,
Возраст. Создать отчетный файл с информацией по количеству людей
входящих в ту или иную возрастную группу. Возрастные группы: 1-12, 13-18,
19-25, 26-40, 40+
"""

import csv
import json

data = []
with open("data_01.csv", "r") as fin:
    f_reader = csv.reader(fin, delimiter=",")
    for row in f_reader:
        data.append(row)
del(data[0])

peoples_in_age_ranges = {"1-12": 0, "13-18": 0, "19-25": 0, "26-40": 0, "40+": 0}

for row in data:
    if int(row[2]) <= 12:
        peoples_in_age_ranges["1-12"] += 1
    elif 12 < int(row[2]) <= 18:
        peoples_in_age_ranges["13-18"] += 1
    elif 18 < int(row[2]) <= 25:
        peoples_in_age_ranges["19-25"] += 1
    elif 25 < int(row[2]) <= 40:
        peoples_in_age_ranges["26-40"] += 1
    else:
        peoples_in_age_ranges["40+"] += 1

with open("data_01.json", "w") as fout:
    json.dump(peoples_in_age_ranges, fout)
