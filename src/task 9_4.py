"""Создать универсальный декоратор, который меняет порядок аргументов в
функции на противоположный"""


def decor_f(func):
    def wrapper(*args):
        func(args[::-1])
    return wrapper


@ decor_f
def list_num():
    print()


list_num(1, 2, 3)
