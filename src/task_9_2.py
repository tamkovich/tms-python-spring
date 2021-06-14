"""
Создать csv файл с данными о ежедневной погоде. Структура: Дата,
Место, Градусы, Скорость ветра. Найти среднюю погоду(скорость ветра и
градусы) для Минск за последние 7 дней.
"""
import csv
from datetime import date
data_now = date.today()
data_sevendays_ago = date(data_now.year, data_now.month, data_now.day - 7)
with open("file_weather.csv", "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    count = 0
    summa_temperature = summa_weed = 0
    for row in csvreader:
        if count != 0 and row[1] == "Minsk":
            row_data = row[0].split('-')
            data_list = date(int(row_data[0]), int(row_data[1]), int(row_data[2]))
            if data_sevendays_ago <= data_list < data_now:
                summa_temperature += int(row[2])
                summa_weed += int(row[3])
        count += 1
    print(f"Средняя температура в Минске за последнее 7 дней: {summa_temperature}")
    print(f"Средняя скорость ветра в Минске за последнее 7 дней: {summa_weed}")
