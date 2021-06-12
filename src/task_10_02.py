""" Задание 10.02
Создать csv файл с данными о ежедневной погоде. Структура: Дата,
Место, Градусы, Скорость ветра. Найти среднюю погоду(скорость ветра и
градусы) для Минск за последние 7 дней.
"""

import csv
from datetime import datetime
from datetime import timedelta

today = datetime.today()
seek_period = timedelta(days=7)

data = []
with open("data_weather.csv", "r") as fin:
    f_reader = csv.reader(fin, delimiter=",")
    for row in f_reader:
        data.append(row)
del (data[0])

weather_minsk = list(filter(lambda row: row if row[1] == "Minsk" else None, data))
weather_minsk = list(
    filter(
        lambda row: row if today - seek_period <= datetime.strptime(row[0], '%Y-%m-%d') <= today
        else None, weather_minsk))

avg_temp = 0
avg_wind_speed = 0

for row in weather_minsk:
    avg_temp += int(row[2])
    avg_wind_speed += int(row[3])

avg_temp /= len(weather_minsk)
avg_wind_speed /= len(weather_minsk)

print(f"The average WIND SPEED for last {seek_period.days} days was {round(avg_wind_speed, 2)} m/s"
      f"\nThe average TEMPERATURE for last {seek_period.days} days was {round(avg_temp, 2)} deg")
