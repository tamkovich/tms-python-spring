from classes import Math
from exceptions import NotValidSymbolException


def calculator():
    while True:
        try:
            a = float(input('Введите первое число: '))
        except ValueError:
            print("Неверный формат. Введите число")
            break

        operator = input('Введите операцию: ')
        if operator not in ('+', '-', '*', '/'):
            raise NotValidSymbolException

        try:
            b = float(input('Введите второе число: '))
        except ValueError:
            print("Неверный формат. Введите число")
            break

        math = Math(a, b)
        if operator == '+':
            print(math.sumarize())

        elif operator == '-':
            print(math.diff())

        elif operator == '/':
            print(math.div())

        elif operator == '*':
            print(math.multiply())
