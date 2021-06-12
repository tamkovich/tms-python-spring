# Создать список поездов. Структура словаря: номер поезда,
# пункт и время прибытия, пункт и время отбытия. Вывести все сведения о поездах,
# время пребывания в пути которых превышает 7 часов 20 минут.[02-7.3-ML02]
# Примечание: данное задание подразумевает самостоятельное изучение принципов работы со
# временем в Python(библиотека datetime)
from datetime import datetime, date, time, timedelta

poezd = [{'nomer': 135,
         'Minsk': datetime(2021, 6, 3, 22, 39),
         'Moskow': datetime(2021, 6, 4, 10)
         }, {'nomer': 131,
         'Minsk': datetime(2021, 6, 3, 16, 48),
         'grodno': datetime(2021, 6, 3, 23, 15)
         }, {'nomer': 133,
         'Minsk': datetime(2021, 6, 3, 10, 39),
         'borisov': datetime(2021, 6, 3, 12)
         }, {'nomer': 134,
         'Minsk': datetime(2021, 6, 3, 8, 40),
         'orsha': datetime(2021, 6, 3, 18, 30)
         }]
c = 2
d = 1
r = datetime(2021, 6, 3, 15, 40) - datetime(2021, 6, 3, 8, 40)
for i in poezd:
    a = i.keys()
    b = 1
    z = list(i.keys())
    travel_time = i[z[c]] - i[z[d]]
    if travel_time > r:
        print(i)
