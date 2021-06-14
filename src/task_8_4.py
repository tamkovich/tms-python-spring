"""
Создать универсальный декоратор, который меняет порядок аргументов в
функции на противоположный.
"""


def decorator_function(func):
    def wrapper(num_list):
        # поменяет порядок элементов на противоположный
        func(num_list[::-1])
    return wrapper


@decorator_function
def list_of_word(num):
    # вывод отформатированный список
    print(num)


n = [1, 5, 4, 7, 8, 12, 20]
list_of_word(n)
