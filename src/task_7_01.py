# Задание 7.1 и 7.2:
# Написать 12 функций по переводу:
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
# Примечание: функция принимает на вход число и возвращает конвертированное число
# 2. Написать программу, со следующим интерфейсом: пользователю предоставляется на
# выбор 12 вариантов перевода(описанных в первой задаче). Пользователь вводит цифру
# от одного до двенадцати. После программа запрашивает ввести численное значение.
# Затем программа выдает конвертированный результат. Использовать функции из первого
# задания. Программа должна быть в бесконечном цикле. Код выхода из программы - “0”.
def inch_in_sm(num):  # Дюймы в сантиметры
    sm = num * 2.54
    return sm


def sm_in_inch(num):  # Сантиметры в дюймы
    inch = num * 0.39370
    return inch


def miles_in_km(num):  # Мили в километры
    km = num / 0.62137
    return km


def km_in_miles(num):  # Километры в мили
    mile = num * 0.62137
    return mile


def funts_in_kilo(num):  # Фунты в килограмы
    kg = num / 2.2046
    return kg


def kilo_in_funts(num):  # Килограмы в фунты
    lb = num * 2.2046
    return lb


def unc_in_gramm(num):  # Унции в граммы
    gramm = num / 0.035274
    return gramm


def gram_in_unc(num):  # Граммы в унции
    oz = num * 0.035274
    return oz


def gal_in_litr(num):  # Галлоны в литры
    litr = num / 0.26417
    return litr


def litr_in_gal(num):  # Литры в галлоны
    gal = num * 0.26417
    return gal


def pint_in_litr(num):  # Пинты в литры
    litr = num / 1.7598
    return litr


def litr_in_pint(num):  # Литры в пинты
    pt = num * 1.7598
    return pt


while True:
    n = int(input("Введите число от 1 до 12 для выбора функции перевода: "))
    if n == 1:
        a = float(input("Введите количество дюймов: "))
        print(f"Сантиметров в {a} дюймах: {inch_in_sm(a)}")
    elif n == 2:
        a = float(input("Введите количество сантиметров: "))
        print(f"Дюймов в {a} сантиметрах: {sm_in_inch(a)}")
    elif n == 3:
        a = float(input("Введите количество миль: "))
        print(f"Километров в {a} милях: {miles_in_km(a)}")
    elif n == 4:
        a = float(input("Введите количество километров: "))
        print(f"Миль в {a} километрах: {km_in_miles(a)}")
    elif n == 5:
        a = float(input("Введите количество фунтов: "))
        print(f"Килограмм в {a} фунтах: {funts_in_kilo(a)}")
    elif n == 6:
        a = float(input("Введите количество килограмм: "))
        print(f"Фунтов в {a} килограммах: {kilo_in_funts(a)}")
    elif n == 7:
        a = float(input("Введите количество унций: "))
        print(f"Грамм в {a} унций: {unc_in_gramm(a)}")
    elif n == 8:
        a = float(input("Введите количество грамм: "))
        print(f"Унций в {a} граммах: {gram_in_unc(a)}")
    elif n == 9:
        a = float(input("Введите количество галлонов: "))
        print(f"Литров в {a} галонах: {gal_in_litr(a)}")
    elif n == 10:
        a = float(input("Введите количество литров: "))
        print(f"Галонов в {a} литрах: {litr_in_gal(a)}")
    elif n == 11:
        a = float(input("Введите количество пинт: "))
        print(f"Литров в {a} пинтах: {pint_in_litr(a)}")
    elif n == 12:
        a = float(input("Введите количество литров: "))
        print(f"Пинт в {a} литрах: {litr_in_pint(a)}")
    elif n == 0:
        break
