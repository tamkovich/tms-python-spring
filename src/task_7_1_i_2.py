# Homework - 07
# task_7_1: Написать 12 функций по переводу:
#               1. Дюймы в сантиметры
#               2. Сантиметры в дюймы
#               3. Мили в километры
#               4. Километры в мили
#               5. Фунты в килограммы
#               6. Килограммы в фунты
#               7. Унции в граммы
#               8. Граммы в унции
#               9. Галлон в литры
#               10. Литры в галлоны
#               11. Пинты в литры
#               12. Литры в пинты
# Примечание: функция принимает на вход число и возвращает конвертированное число

# task_7_2: Написать программу, со следующим интерфейсом: пользователю дается
# на выбор 12 вариантов перевода(описанных в первой задаче). Пользователь вводит цифру
# от одного до двенадцати. После программа запрашивает ввести численное значение.
# Затем программа выдает конвертированный результат. Использовать функции из первого
# задания. Программа должна быть в бесконечном цикле. Код выхода из программы - “0”.
import ast


def inches_to_centimeters(num):
    rez = num * 2.54
    print(f"{num} дюймов = {rez} сантиметров")  # или return rez


def centimeters_to_inches(num):
    rez = num / 2.54
    print(f"{num} сантиметров = {rez} дюймов")  # или return rez


def miles_to_kilometers(num):
    rez = num * 1.609344
    print(f"{num} миль = {rez} километров")  # или return rez


def kilometers_to_miles(num):
    rez = num / 1.609344
    print(f"{num} километров = {rez} миль")  # или return rez


def pounds_to_kilograms(num):
    rez = num / 2.2046226218
    print(f"{num} фунтов = {rez} килограммов")  # или return rez


def kilograms_to_pounds(num):
    rez = num * 2.2046226218
    print(f"{num} килограммов = {rez} фунтов")  # или return rez


def ounces_to_grams(num):
    rez = num * 28.349523125
    print(f"{num} унции = {rez} грамм")  # или return rez


def grams_to_ounce(num):
    rez = num / 28.349523125
    print(f"{num} грамм = {rez} унции")  # или return rez


def gallons_to_liters(num):
    rez = num * 3.785411784
    print(f"{num} американских галлона = {rez} литра")  # или return rez


def liters_to_gallons(num):
    rez = num / 3.785411784
    print(f"{num} литра = {rez} американских галлона")  # или return rez


def pints_to_liters(num):
    rez = num / 2.11338
    print(f"{num} пинты = {rez} литра")  # или return rez


def liters_to_pints(num):
    rez = num * 2.11338
    print(f"{num} литра = {rez} пинты")  # или return rez


print("0 - выход из программы",
      "1 - дюймы в сантиметры",
      "2 - сантиметры в дюймы",
      "3 - мили в километры",
      "4 - километры в мили",
      "5 - фунты в килограммы",
      "6 - килограммы в фунты",
      "7 - унции в граммы",
      "8 - граммы в унции",
      "9 - галлон в литры",
      "10 - литры в галлоны",
      "11 - пинты в литры",
      "12 - литры в пинты", sep="\n")
while True:
    oper = input("Введите номер операции конвертации: ")
    if oper.isdigit():
        oper = int(oper)
    else:
        print("Вводите корректное число номера операции!")
        continue
    if oper == 0:
        break
    num = ast.literal_eval(input("Введите число для конвертации: "))
    if type(num) == float or type(num) == int:
        num = float(num)
    else:
        print("Вы ввели не число, конвертация невозможна!")
        continue
    if oper == 1:
        inches_to_centimeters(num)
    elif oper == 2:
        centimeters_to_inches(num)
    elif oper == 3:
        miles_to_kilometers(num)
    elif oper == 4:
        kilometers_to_miles(num)
    elif oper == 5:
        pounds_to_kilograms(num)
    elif oper == 6:
        kilograms_to_pounds(num)
    elif oper == 7:
        ounces_to_grams(num)
    elif oper == 8:
        grams_to_ounce(num)
    elif oper == 9:
        gallons_to_liters(num)
    elif oper == 10:
        liters_to_gallons(num)
    elif oper == 11:
        pints_to_liters(num)
    elif oper == 12:
        liters_to_pints(num)
