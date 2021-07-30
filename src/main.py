"""
Homework - 13
task_13_2: Выполнить задание 1 с использованием класса Math.
Класс принимает в качестве аргументов два числа.
Определить 4 метода(сложение, вычитание, умножение, деление).
Добавить валидацию входных данных.
Программа должна состоять из четырех файлов
(main.py, classes.py, ui_func.py exceptions.py). [my-oop-t06]
"""

import exceptions
import ui_func

if __name__ == "__main__":
    ui_func.start_calculations()
    exceptions.print_error()
