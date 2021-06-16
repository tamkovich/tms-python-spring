"""Создать декоратор для функции, которая принимает список чисел.
Декоратор должен производить предварительную проверку данных -
удалять все четные элементы из списка"""


def spis_chis(*args):
    spis = args
    print(spis)
    return spis


def decor(func):
    list(func)
    new_spis = list(filter(lambda a: a % 2 != 0, func))
    func = new_spis
    return func


print(decor(spis_chis(6, 5, 7, 8)))


def spis_chis():
    spis = [1, 6, 7, 8]
    print(spis)
    return spis


def decor(func):
    list(func)
    new_spis = list(filter(lambda a: a % 2 == 0, func))
    for i in new_spis:
        func.remove(i)
    return func


print(decor(spis_chis()))
