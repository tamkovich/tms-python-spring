# Задание 3_10
# Получить на ввод количество рублей, копеек и вывести в правильной форме,
# Например: 3 рубля, 1 рубль 25 копеек, 3 копейки

rub = int(input('Введите количество рублей: '))
mon = int(input('Введите количество копеек: '))
mon_1 = str(mon)
rub_1 = str(rub)

if int(mon_1[-1]) > 0 and int(mon_1[-1]) < 2:
    m_str = 'копейка'
if len(mon_1) >= 2 and int(mon_1[-2]) == 1:
    m_str = 'копеек'
elif int(mon_1[-1]) >= 2 and int(mon_1[-1]) < 5:
    m_str = 'копейки'
elif int(mon_1[-1]) >= 5 and int(mon_1[-1]) <= 9 or int(mon_1[-1]) == 0:
    m_str = 'копеек'
if mon < 100:
    if len(rub_1) >= 2 and int(rub_1[-2]) == 1:
        r_str = 'рублей'
    elif int(rub_1[-1]) > 0 and int(rub_1[-1]) < 2:
        r_str = 'рубль'
    elif int(rub_1[-1]) >= 2 and int(rub_1[-1]) < 5:
        r_str = 'рубля'
    elif int(rub_1[-1]) >= 5 and int(rub_1[-1]) <= 9 or int(rub_1[-1]) == 0:
        r_str = 'рублей'
    print(rub_1, r_str, mon, m_str)
if len(mon_1) == 3 and int(mon_1[0:]) >= 101 and int(mon_1[0:]) <= 999:
    rub_2 = int(rub + (mon / 100))
    rub_3 = str(rub_2)
    mon_2 = int(mon_1[1:])
    if len(rub_3) >= 2 and int(rub_3[-2]) == 1:
        r_str = 'рублей'
    elif int(rub_3[-1]) > 0 and int(rub_3[-1]) < 2:
        r_str = 'рубль'
    elif int(rub_3[-1]) >= 2 and int(rub_3[-1]) < 5:
        r_str = 'рубля'
    elif int(rub_3[-1]) >= 5 and int(rub_3[-1]) <= 9 or int(rub_3[-1]) == 0:
        r_str = 'рублей'
    print(rub_3, r_str, mon_2, m_str)
if len(mon_1) > 3 and int(mon_1[-3:]) > 100:
    rub_2 = int(rub + (mon / 100))
    mon_2 = int(mon_1[-2:])
    rub_3 = str(rub_2)
    if int(rub_3[-1]) > 0 and int(rub_3[-1]) < 2:
        r_str = 'рубль'
    elif len(rub_3) >= 2 and int(rub_3[-2]) == 1:
        r_str = 'рублей'
    elif int(rub_3[-1]) >= 2 and int(rub_3[-1]) < 5:
        r_str = 'рубля'
    elif int(rub_3[-1]) >= 5 and int(rub_3[-1]) <= 9 or int(rub_3[-1]) == 0:
        r_str = 'рублей'
    print(rub_3, r_str, mon_2, m_str)
if len(mon_1) > 3 and int(mon_1[-3:]) == 100:
    rub_2 = int(rub + (mon / 100))
    rub_3 = str(rub_2)
    if int(rub_3[-1]) > 0 and int(rub_3[-1]) < 2:
        r_str = 'рубль'
    elif len(rub_3) >= 2 and int(rub_3[-2]) == 1:
        r_str = 'рублей'
    elif int(rub_3[-1]) >= 2 and int(rub_3[-1]) < 5:
        r_str = 'рубля'
    elif int(rub_3[-1]) >= 5 and int(rub_3[-1]) <= 9 or int(rub_3[-1]) == 0:
        r_str = 'рублей'
    print(rub_3, r_str)
if len(mon_1) > 3 and int(mon_1[-3:]) < 100:
    rub_2 = int(rub + (mon / 100))
    mon_2 = int(mon_1[-2:])
    rub_3 = str(rub_2)
    if int(rub_3[-1]) > 0 and int(rub_3[-1]) < 2:
        r_str = 'рубль'
    elif len(rub_3) >= 2 and int(rub_3[-2]) == 1:
        r_str = 'рублей'
    elif int(rub_3[-1]) >= 2 and int(rub_3[-1]) < 5:
        r_str = 'рубля'
    elif int(rub_3[-1]) >= 5 and int(rub_3[-1]) <= 9 or int(rub_3[-1]) == 0:
        r_str = 'рублей'
    print(rub_3, r_str, mon_2, m_str)
if rub == 0 and mon == 0:
    print('No money, no honey!')

# Программа может сама переводить копейки в рубли
# Также программа выводит слова "рубль" и "копейка" с правильными окончаниями
# в зависимости от привязанных к ним чисел
