""" Создать csv файл с данными следующей структуры: Имя, Фамилия,
Возраст. Создать отчетный файл с информацией по количеству людей
входящих в ту или иную возрастную группу. Возрастные группы: 1-12, 13-18,
19-25, 26-40, 40+. """

import csv
import json

fields = ['firstname', 'lastname', 'age']
rows = [['Ivan', 'Iwanov', 5],
        ['Petr', 'Petrov', 10],
        ['Dima', 'Dimasov', 15],
        ['Sveta', "Svetlova", 18],
        ['Vasia', 'Vasiliev', 20],
        ['Toma', 'Tomarovskay', 30],
        ['Ignat', 'Ignatov', 50]
        ]
filename = 'people_info.csv'

with open(filename, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)

dict_res_file = {"1 - 12": 0,
                 "13 - 18": 0,
                 "19 - 25": 0,
                 "26 - 40": 0,
                 "40+": 0}

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        if int(row[2]) < 13:
            dict_res_file["1 - 12"] += 1
        elif int(row[2]) < 19:
            dict_res_file["13 - 18"] += 1
        elif int(row[2]) < 26:
            dict_res_file["19 - 25"] += 1
        elif int(row[2]) < 41:
            dict_res_file["26 - 40"] += 1
        else:
            dict_res_file["40+"] += 1

with open("res_count_people.json", "w") as f_:
    data = json.dumps(dict_res_file)
    f_.write(data)
