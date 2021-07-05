"""functions addition,
subtraction, multiplication and division"""


def add(a, b):
    return f'Результат сложения: {a + b}'


def sub(a, b):
    return f'Результат вычитания: {a - b}'


def mul(a, b):
    return f'Резултат умножения: {a * b}'


def div(a, b):
    try:
        answer = round(a / b, 10)
        return f'Результат деления: {answer}'
    except ZeroDivisionError:
        return 'ZeroDivisionError: division by zero'
