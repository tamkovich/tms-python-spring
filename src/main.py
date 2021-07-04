"""
Выполнить задание 1 с использованием класса Math. Класс принимает в
качестве аргументов два числа. Определить 4 метода(сложение,
вычитание, умножение, деление). Добавить валидацию входных данных.
Программа должна состоять из четырех файлов(main.py, classes.py,
ui_func.py exceptions.py).
"""
import ui_func


list_of_operation = ['+', '-', '*', '/', '0']
while True:
    print("Выберите один из операции: '+", '-', '*', '/')
    print("Для выхода из программы выберите '0'")
    operation = input()
    if operation in list_of_operation and operation != '0':
        num1 = input("Введите первое число:  ")
        num2 = input("Введите втарое число:  ")
        ui_func.fun_calculation(operation, num1, num2)
    elif operation == '0':
        break
    else:
        print("Неправильно выбрано операция")
