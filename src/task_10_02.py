"""Создать csv файл с данными о ежедневной погоде. Структура: Дата,
Место, Градусы, Скорость ветра. Найти среднюю погоду(скорость ветра и
градусы) для Минск за последние 7 дней. """


import csv

fields_weather = ['date', 'location', 'grade', 'wind_speed']
rows_weather = [
    ['2021.01.01', 'Minsk', 5, 50],
    ['2021.01.02', 'Minsk', 10, 70],
    ['2021.01.03', 'Minsk', 15, 60],
    ['2021.01.04', 'Minsk', 18, 88],
    ['2021.01.05', 'Minsk', 20, 65],
    ['2021.01.06', 'Minsk', 30, 56],
    ['2021.01.07', 'Minsk', 5, 50],
    ['2021.01.08', 'Minsk', 10, 70],
    ['2021.01.09', 'Minsk', 15, 60],
    ['2021.01.10', 'Minsk', 18, 88],
    ['2021.01.11', 'Minsk', 20, 65],
    ['2021.01.12', 'Minsk', 30, 56],
    ['2021.01.13', 'Pinsk', 5, 50],
    ['2021.01.14', 'Pinsk', 10, 70],
    ['2021.01.15', 'Pinsk', 15, 60],
    ['2021.01.16', 'Pinsk', 18, 88],
    ['2021.01.17', 'Pinsk', 20, 65],
    ['2021.01.18', 'Pinsk', 30, 56],
    ['2021.01.17', 'Pinsk', 50, 45]
]

filename = 'date_weather.csv'
n = 7
with open(filename, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(fields_weather)
    csvwriter.writerows(rows_weather)

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    counter_minsk_weather = 0
    for row in csvreader:
        if row[1] == 'Minsk':
            counter_minsk_weather += 1

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    average_grade = 0
    average_speed = 0
    counter_minsk = 0
    for row in csvreader:
        if row[1] == 'Minsk':
            counter_minsk += 1
            if counter_minsk >= counter_minsk_weather - (n - 1):
                average_grade += int(row[2])
                average_speed += int(row[3])

print(f"Для Минска за последние 7 дней\n"
      f"средняя температура = {average_grade/n}\n"
      f"средняя скорость ветра = {average_speed/n}")
