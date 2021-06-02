# Создать список поездов. Структура словаря: номер поезда,
# пункт и время прибытия, пункт и время отбытия. Вывести все сведения о поездах,
# время пребывания в пути которых превышает 7 часов 20 минут.

from datetime import datetime, timedelta
trains = [{
        'number': 1,
        'start_time': datetime(2021, 5, 1, 0, 0, 0),
        'start_place': 'town1',
        'arrival_time': datetime(2021, 5, 1, 7, 20, 0),
        'end_place': 'town2',
    },
    {
        'number': 2,
        'start_time': datetime(2021, 5, 1, 0, 0, 0),
        'start_place': 'town1',
        'arrival_time': datetime(2021, 5, 1, 7, 20, 1),
        'end_place': 'town2',
    }, ]
for i in trains:
    if i['arrival_time'] - i['start_time'] > timedelta(hours=7, minutes=20):
        print(f"Train number: {i['number']}")
        print(f"Start place: {i['start_place']}, Start time: {i['start_time']}")
        print(f"End place: {i['end_place']}, Arrival time: {i['arrival_time'] - i['start_time']}")
