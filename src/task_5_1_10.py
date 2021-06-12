# Задание 5.10
# Создать список поездов.
# Структура словаря: номер поезда, пункт и время прибытия, пункт и время отбытия.
# Вывести все сведения о поездах, время пребывания в пути которых превышает 7 часов 20 минут.
# Примечание: данное задание подразумевает самостоятельное изучение принципов работы со
# временем в Python(библиотека datetime)

from datetime import datetime

trains = [
    {'number': 'R205-417',
     'start_point': 'Minsk',
     'start_time': datetime(1, 1, 1, 5, 45),
     'end_point': 'Hrodno',
     'end_time': datetime(1, 1, 1, 9, 27)
     },
    {'number': 'Z100-225',
     'start_point': 'Brest',
     'start_time': datetime(1, 1, 1, 7, 15),
     'end_point': 'Prague',
     'end_time': datetime(1, 1, 1, 20, 25)
     },
    {'number': 'Q117-007',
     'start_point': 'Minsk',
     'start_time': datetime(1, 1, 1, 8, 5),
     'end_point': 'Vilnius',
     'end_time': datetime(1, 1, 1, 11, 5)
     },
    {'number': 'G097-317',
     'start_point': 'Warsaw',
     'start_time': datetime(1, 1, 1, 0, 0),
     'end_point': 'Dusseldorf',
     'end_time': datetime(1, 1, 1, 12, 32)
     },
]

DELTA = 7 * 3600 + 20 * 60  # 7 h 20 min in seconds

print("TRAIN SCHEDULE:\n---------------")
for train in trains:  # Show all
    delta_time = train['end_time'] - train['start_time']
    print(f"{train['number']}: {train['start_point']} - {train['end_point']} | ",
          f"{train['start_time'].hour}:{train['start_time'].minute} - ",
          f"{train['end_time'].hour}:{train['end_time'].minute} | {delta_time}")

print("\nTRAVEL TIME EXCEEDS 7h 20 min:\n------------------------------")
for train in trains:  # Travel time > 7h 20 min
    delta_time = train['end_time'] - train['start_time']
    if delta_time.seconds > DELTA:
        print(f"{train['number']}: {train['start_point']} - {train['end_point']} | ",
              f"{train['start_time'].hour}:{train['start_time'].minute} - ",
              f"{train['end_time'].hour}:{train['end_time'].minute} | {delta_time}")
