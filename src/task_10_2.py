"""
    Программа создает csv файл из списка словарей
    и выводит среднее значение погоды для указаного 
    диапозона дат пользоватеем
"""

import csv
from datetime import datetime, date

# Список словарей для входных данных csv файла
pogoda_city_rb = [
    {
        "date": "2021/6/1",
        "city": "Минск",
        "degrees": 35,
        "speed_wind": 2,
    },
    {
        "date": "2021/6/2",
        "city": "Минск",
        "degrees": 30,
        "speed_wind": 1,
    },
    {
        "date": "2021/6/3",
        "city": "Минск",
        "degrees": 25,
        "speed_wind": 2,
    },
    {
        "date": "2021/6/4",
        "city": "Минск",
        "degrees": 26,
        "speed_wind": 7,
    },
    {
        "date": "2021/6/5",
        "city": "Минск",
        "degrees": 24,
        "speed_wind": 0,
    },
    {
        "date": "2021/6/6",
        "city": "Минск",
        "degrees": 35,
        "speed_wind": 2,
    },
    {
        "date": "2021/6/7",
        "city": "Минск",
        "degrees": 29,
        "speed_wind": 4,
    },
    {
        "date": "2021/6/8",
        "city": "Минск",
        "degrees": 31,
        "speed_wind": 1,
    },
    {
        "date": "2021/6/8",
        "city": "Брест",
        "degrees": 30,
        "speed_wind": 2,
    },
    {
        "date": "2021/6/8",
        "city": "Гродно",
        "degrees": 29,
        "speed_wind": 1,
    },
    {
        "date": "2021/6/8",
        "city": "Витебск",
        "degrees": 25,
        "speed_wind": 4,
    },
    {
        "date": "2021/6/8",
        "city": "Гомель",
        "degrees": 23,
        "speed_wind": 10,
    },
]
# Кортеж заголовков для csv
row_head = ("date", "city", "degrees", "speed_wind")
# Создаем csv файл и передаем в него pogoda_city_rb
with open("pogoda_goroda.csv", "w") as pogoda:
    writer = csv.DictWriter(pogoda, fieldnames=row_head, delimiter=",")
    writer.writeheader()
    writer.writerows(pogoda_city_rb)

# Устанавливаем диапозон дат и город для которых будет расчитываться среднеее значение
date_start = date(2021, 6, 2)
date_finish = date(2021, 6, 8)
city = "Брест"
# Открываем csv файл для чтения
with open("pogoda_goroda.csv", "r") as pogoda_city:
    read = csv.DictReader(pogoda_city)
    avg_degrees = []
    avg_wind_spid = []
    for row in read:
        # Условие для указаного города и диапозонa дат
        if (
            row["city"] == city
            and datetime.strptime(row["date"], "%Y/%m/%d").date() >= date_start
            and datetime.strptime(row["date"], "%Y/%m/%d").date() <= date_finish
        ):
            avg_degrees.append(int(row["degrees"]))
            avg_wind_spid.append(int(row["speed_wind"]))
    # Отлавливаем исключение в случаи если для конкретного города в заданом диапозоне дат нету информации
    try:
        print(
            f"Средняя температура для города {city}: {sum(avg_degrees)/len(avg_degrees)} c"
        )
        print(
            f"Средняя скорость ветра для города {city}: {sum(avg_wind_spid)/len(avg_wind_spid)} m/c"
        )
    except ZeroDivisionError:
        print(f"для указанного диапозона дат города {city}  нету информации")
