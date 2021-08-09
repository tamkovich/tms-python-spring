"""
Написать калькулятор. Программа должна содержать 4 функции
принимающие два аргумента и возвращающие результаты сложения,
вычитания, умножения и деления. Реализовать пользовательский
интерфейс с бесконечным циклом. Добавить валидацию входных данных.
Программа должна состоять из четырех файлов(main.py, func.py, ui_func.py
exceptions.py).
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
        print(ui_func.Calculation(operation, num1, num2))
    elif operation == '0':
        break
    else:
        print("Неправильно выбрано операция")
