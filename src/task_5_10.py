# Создать список поездов. Структура словаря: номер поезда,
# пункт и время прибытия, пункт и время отбытия.
# Вывести все сведения о поездах, время пребывания в пути которых
# превышает 7 часов 20 минут.[02-7.3-ML02]
# Примечание: данное задание подразумевает самостоятельное изучение принципов работы
# со временем в Python(библиотека datetime).

import datetime

trains = [
    {
        'train_number': 321,
        'start_time': datetime.datetime(2021, 3, 14, 16, 50, 0, 0),
        'start_place': 'Moscow',
        'finish_time': datetime.datetime(2021, 3, 15, 20, 52, 0, 0),
        'finish_place': 'Briansk',
    },
    {
        'train_number': 222,
        'start_time': datetime.datetime(2021, 4, 14, 7, 00, 0, 0),
        'start_place': 'Gomel',
        'finish_time': datetime.datetime(2021, 4, 14, 9, 50, 0, 0),
        'finish_place': 'Minsk',
    },
    {
        'train_number': 32,
        'start_time': datetime.datetime(2021, 5, 12, 15, 30, 12, 0),
        'start_place': 'Grodno',
        'finish_time': datetime.datetime(2021, 5, 12, 22, 45, 44, 0),
        'finish_place': 'Vilnus',
    },
    {
        'train_number': 566,
        'start_time': datetime.datetime(2021, 2, 12, 12, 52, 23, 0),
        'start_place': 'Sochi',
        'finish_time': datetime.datetime(2021, 2, 21, 16, 26, 52, 0),
        'finish_place': 'Magadan',
    }
]

time_delta = 7 * 3600 + 20 * 60

print("--------------- Расписание поездов ----------------")
for poezd in trains:
    road_time = poezd['finish_time'] - poezd['start_time']
    print(f"{poezd['train_number']} <> {poezd['start_place']} - {poezd['finish_place']} | ",
          f"{poezd['start_time'].hour}:{poezd['start_time'].minute} - ",
          f"{poezd['finish_time'].hour}:{poezd['finish_time'].minute}: Время в пути: {road_time}")


print("-------------- Долгоидущие --------------")
for poezd in trains:
    road_time = poezd['finish_time'] - poezd['start_time']
    road_time_in_seconds = road_time.total_seconds()
    if road_time_in_seconds > time_delta:
        print(f"{poezd['train_number']} <> {poezd['start_place']} - {poezd['finish_place']} | ",
              f"{poezd['start_time'].hour}:{poezd['start_time'].minute} - ",
              f"{poezd['finish_time'].hour}:{poezd['finish_time'].minute}: Время в пути: {road_time}")
