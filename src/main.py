"""Задача 13.01.
Написать калькулятор. Программа должна содержать 4 функции
принимающие два аргумента и возвращающие результаты сложения,
вычитания, умножения и деления. Реализовать пользовательский
интерфейс с бесконечным циклом. Добавить валидацию входных данных.
Программа должна состоять из четырех файлов(main.py, func.py, ui_func.py
exceptions.py)."""


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
    result = ui.OPERATIONS[choice](a, b)
    print(f"{a} {choice} {b} = {result:.2f}"
          "\n-------------------------------------")

print("Exit program.")
