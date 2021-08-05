""" Задание 9.06
Написать декоратор, который будет выводить время
выполнения функции
from datetime import datetime
time = datetime.now()"""

from datetime import datetime


def decorator_time(func):

    def inner():
        start_ = datetime.now()
        func()
        finish_ = datetime.now()
        time_ = finish_ - start_
        print(f"время выполнения функции = {time_}")

    return inner


@decorator_time
def hello_():
    print([number ** 10 for number in range(9999)])


hello_()
