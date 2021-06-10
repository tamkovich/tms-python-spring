"""
Создать декоратор для функции, которая принимает список чисел.
Декоратор должен производить предварительную проверку данных -
удалять все четные элементы из списка.
"""


def decor(func):
    def wrap(*nums):
        new_nums = [a for a in nums if a % 2]
        return func(new_nums)

    return wrap


@decor
def real_func(x):
    print(x)


print(real_func(1, 2, 3, 4, 5, 6, 7, 53, 52))
