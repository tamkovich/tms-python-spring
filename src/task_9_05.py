""" Задание 9.06 (из презентации к занятию)
Написать декоратор, который будет выводить время
выполнения функции
"""

from datetime import datetime
from functools import reduce
from time import sleep


def time_checker(real_func):
    """The decorator trace and print the run time of the function"""
    def wrapper(*args, **kwargs):
        time_start = datetime.now()
        real_func(*args, **kwargs)
        time_end = datetime.now()
        print(f"Run time is {(time_end - time_start).microseconds} ms")
    return wrapper


@time_checker
def my_func():
    """The function count the product of the elements of a sequence that are multiples of 3"""
    init_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    filtered_data = list(filter(lambda n: n % 3 == 0, init_data))
    print(filtered_data)

    product = reduce(lambda n_prev, n: n_prev * n, filtered_data)
    print(product)
    sleep(0.25)  # Delay 0.25 sec


my_func()
