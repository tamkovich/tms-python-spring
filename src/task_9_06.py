"""Задание 9.06
Написать декоратор, который будет выводить время
выполнения функции"""

from datetime import datetime


def sum_():
    i = 0
    b = []
    while i < 10002:
        b.append('iyugefiufasgfwagui')
        i += 1
    print(b)


def decor(func):
    time_1 = datetime.now()
    func()
    time_2 = datetime.now()
    delta = time_2 - time_1
    return f'время выполнения функции - {delta}'


print(decor(sum_))
