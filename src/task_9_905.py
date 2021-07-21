"""
Homework - 09
task_9_905: Дан список чисел. Найти произведение всех чисел, которые кратны 3.
"""
from functools import reduce

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
res = reduce(lambda a, b: a * b, (filter(lambda x: x % 3 == 0, my_list)))
print(res)
