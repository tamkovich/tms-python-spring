# 1. Написать 12 функций по переводу:
# 1. Дюймы в сантиметры
# 2. Сантиметры в дюймы
# 3. Мили в километры
# 4. Километры в мили
# 5. Фунты в килограммы
# 6. Килограммы в фунты
# 7. Унции в граммы
# 8. Граммы в унции
# 9. Галлон в литры
# 10. Литры в галлоны
# 11. Пинты в литры
# 12. Литры в пинты
# Примечание: функция принимает на вход число и возвращает конвертированное число.


def inch_to_centimeters(inch):
    cm = inch / 2.54
    return cm


def centimetres_to_inch(cm):
    inch = cm * 2.54
    return inch


def miles_to_km(mil):
    km = mil / 1.61
    return km


def km_to_miles(km):
    mil = km * 1.61
    return mil


def pounds_to_kg(pounds):
    kg = pounds * 2.2
    return kg


def kg_to_pounds(kg):
    pounds = kg / 2.2
    return pounds


def ounce_to_gram(ou):
    gram = ou * 28.34
    return gram


def gram_to_ounce(gr):
    ounce = gr / 28.34
    return ounce


def gall_to_liter(gl):
    liter = gl / 3.79
    return liter


def liter_to_gall(lt):
    gall = lt * 3.79
    return gall


def pints_to_liter(pint):
    liter = pint / 1.76
    return liter


def liter_to_pints(liter):
    pint = liter * 1.76
    return pint


# 2. Написать программу, со следующим интерфейсом:
# пользователю предоставляется на выбор 12 вариантов перевода(описанных в первой задаче).
# Пользователь вводит цифру от одного до двенадцати.
# После программа запрашивает ввести численное значение.
# Затем программа выдает конвертированный результат.
# Использовать функции из первого задания.
# Программа должна быть в бесконечном цикле. Код выхода из программы - “0”.

while True:
    print(f'---------------------',
          f'1. Дюймы в сантиметры',
          f'2. Сантиметры в дюймы',
          f'3. Мили в километры',
          f'4. Километры в мили',
          f'5. Фунты в килограммы',
          f'6. Килограммы в фунты',
          f'7. Унции в граммы',
          f'8. Граммы в унции',
          f'9. Галлон в литры',
          f'10. Литры в галлоны',
          f'11. Пинты в литры',
          f'12. Литры в пинты',
          f'---------------------', sep='\n')
    x = (input(f'Введите номер операции: '))
    while True:
        if not x.isdigit():
            print('Ошибка! Введите номер операции: ')
            x = (input('Введите номер операции: '))
        else:
            break
    k = float(x)
    if k == 1:
        print(inch_to_centimeters(float(input(f'Введите число, дюймы: '))), 'см')
    elif k == 2:
        print(centimetres_to_inch(float(input(f'Введите число, см: '))), 'inches')
    elif k == 3:
        print(miles_to_km(float(input(f'Введите число, км: '))), 'miles')
    elif k == 4:
        print(km_to_miles(float(input(f'Введите число, мили: '))), 'km')
    elif k == 5:
        print(pounds_to_kg(float(input(f'Введите число, фунты: '))), 'kg')
    elif k == 6:
        print(kg_to_pounds(float(input(f'Введите число, кг: '))), 'pounds')
    elif k == 7:
        print(ounce_to_gram(float(input(f'Введите число, унции: '))), 'ounce')
    elif k == 8:
        print(gram_to_ounce(float(input(f'Введите число, гр: '))), 'gram')
    elif k == 9:
        print(gall_to_liter(float(input(f'Введите число, галлоны: '))), 'gallon')
    elif k == 10:
        print(liter_to_gall(float(input(f'Введите число, литры: '))), 'liters')
    elif k == 11:
        print(pints_to_liter(float(input(f'Введите число, пинты: '))), 'pints')
    elif k == 12:
        print(liter_to_pints(float(input(f'Введите число: '))), 'liters')
    elif k == 0:
        print('Программа завершена')
        break
