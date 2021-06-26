"""Задача 13.02.
Выполнить задание 1 с использованием класса Math. Класс принимает в
качестве аргументов два числа. Определить 4 метода(сложение,
вычитание, умножение, деление). Добавить валидацию входных данных.
Программа должна состоять из четырех файлов(main.py, classes.py,
ui_func.py exceptions.py)."""


from classes import Math
from exceptions import OperationTypeException
import ui_func as ui

while True:
    try:
        choice = ui.get_user_choice()
    except OperationTypeException as error:
        print(f"\nAn error has occurred. {error}\n")
        choice = "0"

    if choice == "0":
        break
    a, b = ui.get_operands()
    math = Math(a, b)
    result = ui.calculate(choice, math)
    print(f"{a} {choice} {b} = {result:.2f}"
          "\n-------------------------------------")

print("Exit program.")
