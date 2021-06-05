# Задание 3_10
# Получить на ввод количество рублей, копеек и вывести в правильной форме,
# Например: 3 рубля, 1 рубль 25 копеек, 3 копейки

while True:
    try:
        rub_str = input('Введите количество рублей: ')
        mon_str = input('Введите количество копеек: ')
        mon_int = int(mon_str)
        rub_int = int(rub_str)

        if int(mon_str[-1]) > 0 and int(mon_str[-1]) < 2:
            mon_rezult = 'копейка'
        if len(mon_str) >= 2 and int(mon_str[-2]) == 1:
            mon_rezult = 'копеек'
        elif int(mon_str[-1]) >= 2 and int(mon_str[-1]) < 5:
            mon_rezult = 'копейки'
        elif int(mon_str[-1]) >= 5 and int(mon_str[-1]) <= 9 or int(mon_str[-1]) == 0:
            mon_rezult = 'копеек'
        if mon_int < 100:
            if len(rub_str) >= 2 and int(rub_str[-2]) == 1:
                rub_rezult = 'рублей'
            elif int(rub_str[-1]) > 0 and int(rub_str[-1]) < 2:
                rub_rezult = 'рубль'
            elif int(rub_str[-1]) >= 2 and int(rub_str[-1]) < 5:
                rub_rezult = 'рубля'
            elif int(rub_str[-1]) >= 5 and int(rub_str[-1]) <= 9 or int(rub_str[-1]) == 0:
                rub_rezult = 'рублей'
            print(rub_str, rub_rezult, mon_int, mon_rezult)
        if len(mon_str) == 3 and int(mon_str[0:]) >= 101 and int(mon_str[0:]) <= 999:
            rub_int_2 = int(rub_int + (mon_int / 100))
            rub_str_2 = str(rub_int_2)
            mon_int_2 = int(mon_str[1:])
            if len(rub_str_2) >= 2 and int(rub_str_2[-2]) == 1:
                rub_rezult = 'рублей'
            elif int(rub_str_2[-1]) > 0 and int(rub_str_2[-1]) < 2:
                rub_rezult = 'рубль'
            elif int(rub_str_2[-1]) >= 2 and int(rub_str_2[-1]) < 5:
                rub_rezult = 'рубля'
            elif int(rub_str_2[-1]) >= 5 and int(rub_str_2[-1]) <= 9 or int(rub_str_2[-1]) == 0:
                rub_rezult = 'рублей'
            print(rub_str_2, rub_rezult, mon_int_2, mon_rezult)
        if len(mon_str) > 3 and int(mon_str[-3:]) > 100:
            rub_int_2 = int(rub_int + (mon_int / 100))
            mon_int_2 = int(mon_str[-2:])
            rub_str_2 = str(rub_int_2)
            if len(rub_str_2) >= 2 and int(rub_str_2[-2]) == 1:
                rub_rezult = 'рублей'
            elif int(rub_str_2[-1]) > 0 and int(rub_str_2[-1]) < 2:
                rub_rezult = 'рубль'
            elif int(rub_str_2[-1]) >= 2 and int(rub_str_2[-1]) < 5:
                rub_rezult = 'рубля'
            elif int(rub_str_2[-1]) >= 5 and int(rub_str_2[-1]) <= 9 or int(rub_str_2[-1]) == 0:
                rub_rezult = 'рублей'
            print(rub_str_2, rub_rezult, mon_int_2, mon_rezult)
        if len(mon_str) > 3 and int(mon_str[-3:]) == 100:
            rub_int_2 = int(rub_int + (mon_int / 100))
            rub_str_2 = str(rub_int_2)
            if len(rub_str_2) >= 2 and int(rub_str_2[-2]) == 1:
                rub_rezult = 'рублей'
            elif int(rub_str_2[-1]) > 0 and int(rub_str_2[-1]) < 2:
                rub_rezult = 'рубль'
            elif int(rub_str_2[-1]) >= 2 and int(rub_str_2[-1]) < 5:
                rub_rezult = 'рубля'
            elif int(rub_str_2[-1]) >= 5 and int(rub_str_2[-1]) <= 9 or int(rub_str_2[-1]) == 0:
                rub_rezult = 'рублей'
            print(rub_str_2, rub_rezult)
        if len(mon_str) > 3 and int(mon_str[-3:]) < 100:
            rub_int_2 = int(rub_int + (mon_int / 100))
            mon_int_2 = int(mon_str[-2:])
            rub_str_2 = str(rub_int_2)
            if len(rub_str_2) >= 2 and int(rub_str_2[-2]) == 1:
                rub_rezult = 'рублей'
            elif int(rub_str_2[-1]) > 0 and int(rub_str_2[-1]) < 2:
                rub_rezult = 'рубль'
            elif int(rub_str_2[-1]) >= 2 and int(rub_str_2[-1]) < 5:
                rub_rezult = 'рубля'
            elif int(rub_str_2[-1]) >= 5 and int(rub_str_2[-1]) <= 9 or int(rub_str_2[-1]) == 0:
                rub_rezult = 'рублей'
            print(rub_str_2, rub_rezult, mon_int_2, mon_rezult)
        if rub_int == 0 and mon_int == 0:
            print('No money, no honey!')
    except(ValueError):
        print('Вы ввели некорректные данные. Программа работает только с целыми положительными числами.'
              'Попробуйте заново.')

# Программа может сама переводить копейки в рубли
# Также программа выводит слова "рубль" и "копейка" с правильными окончаниями
# в зависимости от привязанных к ним чисел
