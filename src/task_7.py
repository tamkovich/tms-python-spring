"""1. Написать 12 функций по переводу:"""


def func_dm_sm(s):
    """1. Дюймы в сантиметры"""
    number = s * 2.54
    print(f'{s} дюймов = {number} сантиметров')
    return number


def func_sm_dm(s):
    """2. Сантиметры в дюймы"""
    number = s / 2.54
    print(f'{s} сантиметров = {number} дюймов')
    return number


def func_ml_km(s):
    """3. Мили в километры"""
    number = s * 1.6
    print(f'{s} миль = {number} километров')
    return number


def func_km_ml(s):
    """4. Километры в мили"""
    number = s / 1.6
    print(f'{s} километров  = {number} миль ')
    return number


def func_lb_kg(s):
    """5. Фунты в килограммы"""
    number = s / 2.2046
    print(f'{s} фунтов  = {number} килограммов')
    return number


def func_kg_lb(s):
    """6. Килограммы в фунты"""
    number = s * 2.2046
    print(f'{s} килограммов   = {number} фунтов ')
    return number


def func_oz_g(s):
    """7. Унции в граммы"""
    number = s / 0.035274
    print(f'{s} унций   = {number} грамм ')
    return number


def func_g_oz(s):
    """8. Граммы в унции"""
    number = s * 0.035274
    print(f'{s} грамм  = {number} унций ')
    return number


def func_gal_l(s):
    """9. Галлон в литры"""
    number = s * 3.7854
    print(f'{s} галлонов  = {number} литров ')
    return number


def func_l_gal(s):
    """10. Литры в галлоны"""
    number = s / 3.7854
    print(f'{s} литров  = {number} галлонов ')
    return number


def func_p_l(s):
    """11. Пинты в литры"""
    number = s * 0.4732
    print(f'{s} пинта  = {number} литров ')
    return number


def func_l_p(s):
    """12. Литры в пинты"""
    number = s / 0.4732
    print(f'{s} пинта  = {number} литров ')
    return number


func_dm_sm(5)
func_sm_dm(3)
func_ml_km(10)
func_km_ml(16)
func_lb_kg(35)
func_kg_lb(57)
func_oz_g(68)
func_g_oz(7)
func_l_gal(32)
func_gal_l(7)
func_p_l(89)
func_l_p(108)
"""Примечание: функция принимает на вход число и возвращает конвертированное число"""

"""2. Написать программу, со следующим интерфейсом: пользователю предоставляется на
выбор 12 вариантов перевода(описанных в первой задаче). Пользователь вводит цифру
от одного до двенадцати. После программа запрашивает ввести численное значение.
Затем программа выдает конвертированный результат. Использовать функции из первого
задания. Программа должна быть в бесконечном цикле. Код выхода из программы - “0”."""
convertors = {
    1: func_dm_sm,
    2: func_sm_dm,
    3: func_ml_km,
    4: func_km_ml,
    5: func_lb_kg,
    6: func_kg_lb,
    7: func_oz_g,
    8: func_g_oz,
    9: func_gal_l,
    10: func_l_gal,
    11: func_p_l,
    12: func_l_p
}
print(convertors)
while True:
    sign = int(input("Введите код операции(1-12): "))
    if sign == 0:
        print("Выход из программы")
        break
    s = float(input("Введите число: "))
    if sign == 1:
        print(func_dm_sm(s))
    elif sign == 2:
        print(func_sm_dm(s))
    elif sign == 3:
        print(func_ml_km(s))
    elif sign == 4:
        print(func_km_ml(s))
    elif sign == 5:
        print(func_lb_kg(s))
    elif sign == 6:
        print(func_kg_lb(s))
    elif sign == 7:
        print(func_oz_g(s))
    elif sign == 8:
        print(func_g_oz(s))
    elif sign == 9:
        print(func_gal_l(s))
    elif sign == 10:
        print(func_l_gal(s))
    elif sign == 10:
        print(func_l_gal(s))
    elif sign == 11:
        print(func_p_l(s))
    elif sign == 12:
        print(func_l_p(s))
    else:
        print("Неверный код операции")
