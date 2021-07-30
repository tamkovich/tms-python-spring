"""
Создать csv файл с данными следующей структуры: Имя, Фамилия,
Возраст. Создать отчетный файл с информацией по количеству людей
входящих в ту или иную возрастную группу. Возрастные группы: 1-12, 13-18,
19-25, 26-40, 40+
"""
import csv
import json
data = {"1 - 12": 0, "13 - 18": 0, "19 - 25": 0, "26 - 40": 0, "40+": 0}
with open('file_people.csv', encoding="utf8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    count = 0
    for row in csvreader:
        if count != 0:
            age = int(row[2])
            if age <= 12:
                data["1 - 12"] += 1
            elif age <= 18:
                data['13 - 18'] += 1
            elif age <= 25:
                data['19 - 25'] += 1
            elif age <= 40:
                data['26 - 40'] += 1
            else:
                data['40+'] += 1
        count += 1
with open("people.json", "w") as f:
    json.dump(data, f)
