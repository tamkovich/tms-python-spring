# Homework - 05
# task_5_10: Создать список поездов. Структура словаря: номер поезда, пункт и время прибытия,
# пункт и время отбытия. Вывести все сведения о поездах,время пребывания в пути которых
# превышает 7 часов 20 минут.[02-7.3-ML02]
# Примечание: задание подразумевает самостоятельное изучение работы со временем (библ. datetime)

import datetime

spis_poezdov = [
    {"номер поезда": 1,
     "пункт прибытия": "Берлин",
     "время прибытия": "24.06.2021 08:00",
     "пункт отбытия": "Минск",
     "время отбытия": "23.06.2021 22:00"},  # 10 часов
    {"номер поезда": 3,
     "пункт прибытия": "Гродно",
     "время прибытия": "23.06.2021 23:15",
     "пункт отбытия": "Минск",
     "время отбытия": "23.06.2021 20:00"},  # 3 часа 15 минут
    {"номер поезда": 5,
     "пункт прибытия": "Москва",
     "время прибытия": "23.06.2021 17:30",
     "пункт отбытия": "Минск",
     "время отбытия": "23.06.2021 7:00"},  # 10 часов 30 минут
    {"номер поезда": 8,
     "пункт прибытия": "Луна",
     "время прибытия": "13.12.2021 13:13",
     "пункт отбытия": "Минск",
     "время отбытия": "13.12.2021 03:03"},  # 10 часов 10 минут
]
for i in spis_poezdov:
    time_otpr = datetime.datetime.strptime(i["время отбытия"], "%d.%m.%Y %H:%M")
    time_prib = datetime.datetime.strptime(i["время прибытия"], "%d.%m.%Y %H:%M")
    delta = time_prib - time_otpr
    if delta.seconds > 26400:
        print(f"Поезд: {i}")
        print(f"Время в пути: {delta}")
