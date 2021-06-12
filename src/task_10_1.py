"""
    программа создает файл csv вносит в его значения
    на основании этих значений формирует отчетный файл
    какие люди входят в каку возрастную группу
"""
import csv

# Список наименование колонок в csv
row = ["first_name", "last_name", "age"]
# Список с Именами фамилиями и возрастом
list_value = [
    {"first_name": "Cергей", "last_name": "Петров", "age": 25},
    {"first_name": "Андрей", "last_name": "Пупкин", "age": 34},
    {"first_name": "Антон", "last_name": "Иванов", "age": 55},
    {"first_name": "Егор", "last_name": "Лобырин", "age": 26},
    {"first_name": "Миша", "last_name": "Минский", "age": 40},
]

# Создаем и открываем для записи новый csv файл
with open("new_file.csv", "w") as file_csv:
    # Вызываем экземпляр класса DictWriter передаем в конструктор атрибуты
    write = csv.DictWriter(file_csv, delimiter=",", fieldnames=row)
    # Вызываем метод класса DictWriter  writeheader который устанавливает заголовки в csv
    write.writeheader()
    """
        Вызываем метод writerows в который передаем список словарей 
        list_value который создает строки со значениями в csv файле
    """
    write.writerows(list_value)

#  открываем для чтения файл csv
with open("new_file.csv", "r") as file_csv:
    """
        Вызываем экземпляр класса DictReader котрый позволяет формировать 
        список словарей из csv, передаем в конструктор атрибуты
    """
    read = csv.DictReader(file_csv)
    # Создаем и открывайм файл отчет
    with open("new_report.txt", "w") as report:
        """
        Задаем уловия формирования отчета
        по возрастным групам и передаем их
        на запись в файл отчет
        """
        for row in read:
            if int(row["age"]) >= 1 and int(row["age"]) <= 12:
                report.write(
                    f"{row['first_name']} {row['last_name']} возростная группа 1-12 лет ему {row['age']} лет \n"
                )
            elif int(row["age"]) > 12 and int(row["age"]) <= 18:
                report.write(
                    f"{row['first_name']} {row['last_name']} возростная группа 13-18 лет ему {row['age']} лет \n"
                )
            elif int(row["age"]) > 18 and int(row["age"]) <= 25:
                report.write(
                    f"{row['first_name']} {row['last_name']} возростная группа 19-25 лет ему {row['age']} лет \n"
                )
            elif int(row["age"]) > 25 and int(row["age"]) <= 40:
                report.write(
                    f"{row['first_name']} {row['last_name']} возростная группа 26-40 лет ему {row['age']} лет \n"
                )
            elif int(row["age"]) > 40:
                report.write(
                    f"{row['first_name']} {row['last_name']} возростная группа 40+ лет ему {row['age']} лет \n"
                )
