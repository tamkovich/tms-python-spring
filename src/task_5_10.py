"""
Создать список поездов. Структура словаря: номер поезда,
пункт и время прибытия, пункт и время отбытия.
Вывести все сведения о поездах, время пребывания в пути которых превышает 7 часов 20 минут
"""
from datetime import datetime
poezd = [
    {
        'number_poezd': 223,
        'begin_time': datetime(2021, 7, 6, 4, 45, 0),
        'begin_place': 'Сосногорск',
        'end_time': datetime(2021, 7, 6, 9, 12, 0),
        'end_place': 'Москва',
    },
    {
        'number_poezd': 187,
        'begin_time': datetime(2021, 7, 10, 19, 15, 0),
        'begin_place': 'Архагельск',
        'end_time': datetime(2021, 7, 11, 22, 40, 0),
        'end_place': 'Новороссийск',
    },
    {
        'number_poezd':  261,
        'begin_time': datetime(2021, 8, 1, 5, 54, 0),
        'begin_place': 'Архагельск',
        'end_time': datetime(2021, 8, 3, 16, 43, 0),
        'end_place': 'Адлер',
    },
]
for index in poezd:
    different = index['end_time'] - index['begin_time']
    duration_in_s = different.total_seconds()
    minutes = divmod(duration_in_s, 60)[0]
    if minutes > 7 * 60 + 20:
        print(f"Номер поезда: {index['number_poezd']}")
        print(f"Пункт: {index['begin_place']}, Время отбытия: {index['begin_time']}")
        print(f"Пункт: {index['end_place']}, Время прибытия: {index['end_time']}\n")
