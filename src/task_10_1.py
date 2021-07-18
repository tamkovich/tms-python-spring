"""
Homework - 10
task_10_1: Создать csv файл с данными следующей структуры: Имя, Фамилия,
Возраст. Создать отчетный файл с информацией по количеству людей
входящих в ту или иную возрастную группу. Возрастные группы: 1-12, 13-18,
19-25, 26-40, 40+.
"""

from csv_utils import age_classification_csv
from csv_utils import write_csv
import json

write_csv([["Имя", "Фамилия", "Возраст"],
           ["Иванов", "Иван", 20],
           ["Иванов", "Сергей", 14],
           ["Иванов", "Максим", 31],
           ["Петров", "Петр", 3],
           ["Петров", "Илья", 101],
           ["Петров", "Никита", 24],
           ["Сидоров", "Макар", 15],
           ["Сидоров", "Сергей", 23],
           ["Васечкин", "Василий", 28]],
          "people_inf.csv")

file_age_class = age_classification_csv("people_inf.csv")
print(file_age_class)

with open("people_report.json", "w") as f19:
    data = json.dumps(file_age_class)
    f19.write(data)
