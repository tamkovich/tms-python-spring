""" Задача 9.3.
Создать декоратор для функции, которая принимает список чисел.
Декоратор должен производить предварительную проверку данных -
удалять все четные элементы из списка
"""


def arg_checker(func):
    """The decorator exclude the even elements from the list of arguments"""
    def wrapper(*args):
        new_args = list(filter(lambda arg: arg % 2 != 0, args))
        func(*new_args)
    return wrapper


@arg_checker
def print_args(*args):
    """The function takes in a list of int and print it"""
    print(args)


print_args(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
