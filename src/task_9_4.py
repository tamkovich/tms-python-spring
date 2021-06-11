"""
Создать универсальный декоратор, который меняет порядок аргументов в функции на противоположный.
"""


def decor(func):
    return func()[::-1]


@decor
def argum():
    numbs = ['krokodil', 'cat', 'dog', 4, 42, 5435, 6]
    return numbs


print(argum)
