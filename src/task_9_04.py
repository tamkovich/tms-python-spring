""" Задача 9.4
Создать универсальный декоратор, который меняет порядок аргументов в
функции на противоположный."""


def arg_reverser(func):
    """The decorator reverse the list of arguments"""
    def wrapper(*args):
        func(*args[::-1])
    return wrapper


@arg_reverser
def print_args(*args):
    """The function takes in a list of arguments and print it"""
    print(args)


print_args(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
