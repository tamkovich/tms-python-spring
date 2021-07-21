"""
Homework - 07
task_7_1: Написать 12 функций по переводу:
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

task_7_2: Написать программу, со следующим интерфейсом: пользователю дается
на выбор 12 вариантов перевода(описанных в первой задаче). Пользователь вводит цифру
от одного до двенадцати. После программа запрашивает ввести численное значение.
Затем программа выдает конвертированный результат. Использовать функции из первого
задания. Программа должна быть в бесконечном цикле. Код выхода из программы - “0”.
"""


def inches_to_centimeters(numb: float) -> None:
    """Ф-ция переводит дюймы в сантиметры и выводит результат"""
    rez = numb * 2.54
    print(f"{numb} дюймов = {rez} сантиметров")  # или return rez


def centimeters_to_inches(numb: float) -> None:
    """Ф-ция переводит сантиметры в дюймы и выводит результат"""
    rez = numb / 2.54
    print(f"{numb} сантиметров = {rez} дюймов")  # или return rez


def miles_to_kilometers(numb: float) -> None:
    """Ф-ция переводит мили в километры и выводит результат"""
    rez = numb * 1.609344
    print(f"{numb} миль = {rez} километров")  # или return rez


def kilometers_to_miles(numb: float) -> None:
    """Ф-ция переводит километры в мили и выводит результат"""
    rez = numb / 1.609344
    print(f"{numb} километров = {rez} миль")  # или return rez


def pounds_to_kilograms(numb: float) -> None:
    """Ф-ция переводит фунты в килограммы и выводит результат"""
    rez = numb / 2.2046226218
    print(f"{numb} фунтов = {rez} килограммов")  # или return rez


def kilograms_to_pounds(numb: float) -> None:
    """Ф-ция переводит килограммы в фунты и выводит результат"""
    rez = numb * 2.2046226218
    print(f"{numb} килограммов = {rez} фунтов")  # или return rez


def ounces_to_grams(numb: float) -> None:
    """Ф-ция переводит унции в граммы и выводит результат"""
    rez = numb * 28.349523125
    print(f"{numb} унции = {rez} грамм")  # или return rez


def grams_to_ounce(numb: float) -> None:
    """Ф-ция переводит граммы в унции и выводит результат"""
    rez = numb / 28.349523125
    print(f"{numb} грамм = {rez} унции")  # или return rez


def gallons_to_liters(numb: float) -> None:
    """Ф-ция переводит амер.галлоны в литры и выводит результат"""
    rez = numb * 3.785411784
    print(f"{numb} американских галлона = {rez} литра")  # или return rez


def liters_to_gallons(numb: float) -> None:
    """Ф-ция переводит литры в амер.галлоны и выводит результат"""
    rez = numb / 3.785411784
    print(f"{numb} литра = {rez} американских галлона")  # или return rez


def pints_to_liters(numb: float) -> None:
    """Ф-ция переводит пинты в литры и выводит результат"""
    rez = numb / 2.11338
    print(f"{numb} пинты = {rez} литра")  # или return rez


def liters_to_pints(numb: float) -> None:
    """Ф-ция переводит литры в пинты и выводит результат"""
    rez = numb * 2.11338
    print(f"{numb} литра = {rez} пинты")  # или return rez


dict_operation = {
    1: inches_to_centimeters,
    2: centimeters_to_inches,
    3: miles_to_kilometers,
    4: kilometers_to_miles,
    5: pounds_to_kilograms,
    6: kilograms_to_pounds,
    7: ounces_to_grams,
    8: grams_to_ounce,
    9: gallons_to_liters,
    10: liters_to_gallons,
    11: pints_to_liters,
    12: liters_to_pints
}

if __name__ == "__main__":
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
        operation = input("Введите номер операции конвертации: ")
        try:
            operation = int(operation)
        except ValueError:
            print("Вводите корректное число номера операции!")
            continue
        if operation == 0:
            break
        num = input("Введите число для конвертации: ")
        try:
            num = float(num)
            dict_operation[operation](num)
        except ValueError:
            print("Вы ввели не число, конвертация невозможна!")
            continue
        except KeyError:
            print("Введенный номер операции не доступен!")
            continue
