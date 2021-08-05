"""Примечание: Все задания выполнять в одном файле.

1. Написать 12 функций по переводу:

1. Дюймы в сантиметры
2. Сантиметры в дюймы
3. Мили в километры
4. Километры в мили
5. Фунты в килограммы
6. Килограммы в фунты
7. Унции в граммы
8. Граммы в унции
9. Галлон в литры
10. Литры в галлоны
11. Пинты в литры
12. Литры в пинты
Примечание: функция принимает на вход число и возвращает конвертированное число

2. Написать программу, со следующим интерфейсом: пользователю предоставляется на
выбор 12 вариантов перевода(описанных в первой задаче). Пользователь вводит цифру
от одного до двенадцати. После программа запрашивает ввести численное значение.
Затем программа выдает конвертированный результат. Использовать функции из первого
задания. Программа должна быть в бесконечном цикле. Код выхода из программы - “0”."""

def inches_in_centimeters(number_):
    result_ = number_ * 2.54
    return result_

def centimeters_in_inches(number_):
    result_ = number_ / 2.54
    return result_

def miles_in_kilometers(number_):
    result_ = number_ * 1.609
    return result_

def kilometers_in_miles(number_):
    result_ = number_ / 1.609
    return result_

def pounds_in_kilograms(number_):
    result_ = number_ * 0.45359237
    return result_

def kilograms_in_pounds(number_):
    result_ = number_ / 0.45359237
    return result_

def intions_in_grams(number_):
    result_ = number_ * 28.3
    return result_

def grams_in_intions(number_):
    result_ = number_ / 28.3
    return result_

def gallons_in_liters(number_):
    result_ = number_ * 3.7854
    return result_

def liters_in_gallons(number_):
    result_ = number_ / 3.7854
    return result_

def pints_in_liters(number_):
    result_ = number_ * 0.5683
    return result_

def liters_in_pints(number_):
    result_ = number_ / 0.5683
    return result_

var_perevoda = {1: inches_in_centimeters,
                2: centimeters_in_inches,
                3: miles_in_kilometers,
                4: kilometers_in_miles,
                5: pounds_in_kilograms,
                6: kilograms_in_pounds,
                7: intions_in_grams,
                8: grams_in_intions,
                9: gallons_in_liters,
                10: liters_in_gallons,
                11: pints_in_liters,
                12: liters_in_pints}

while True:
    num_comand = int(input("Введите цифру от 0 до 12, где:\n"
                           "0 - выход из программы\n"
                           "1 - перевод дюймов в сантиметры\n"
                           "2 - перевод сантиметров в дюймы\n"
                           "3 - перевод миль в километры\n"
                           "4 - перевод километров в мили\n"
                           "5 - перевод фунтов в килограммы\n"
                           "6 - перевод килограммов в фунты\n"
                           "7 - перевод унций в граммы\n"
                           "8 - перевод граммов в унции\n"
                           "9 - первод галлонов в литры\n"
                           "10 - перевод литров в галлоны\n"
                           "11 - перевод пинт в литры\n"
                           "12 - перевод литров в пинты\n"
                           ">>>>> : "))
    if num_comand == 0:
        break
    else:
        for num_, funk_ in var_perevoda.items():
            if num_comand == int(num_):
                a_number = int(input("Введите числовое значение: "))
                print(funk_(a_number))
print("The End")
