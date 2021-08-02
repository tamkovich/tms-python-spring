"""
Создать универсальный декоратор, который меняет порядок аргументов в
функции на противоположный.
"""


def decorator(func):
    def zamena(x, y):
        x, y = y, x
        func(x, y)
    return zamena


@decorator
def div(x: int, y: int):
    res = x / y
    print(res)
