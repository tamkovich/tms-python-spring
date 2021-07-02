# Выполнить задание 1 с использованием класса Math. Класс принимает в
# качестве аргументов два числа. Определить 4 метода(сложение,
# вычитание, умножение, деление). Добавить валидацию входных данных.
# Программа должна состоять из четырех файлов(main.py, classes.py,
# ui_func.py exceptions.py).
from classes import Math
from ui_func import ui_func


flag = True
while flag:
    print(Math(*ui_func()))
    repeat = input("Would you like to continue? (yes / no)")
    if repeat == "no":
        flag = False
