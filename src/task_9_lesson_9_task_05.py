""" Задание 9.05
Дан список чисел. Найти произведение всех
чисел, которые кратны 3."""

from functools import reduce
result = reduce(lambda a, x: x * a, filter(lambda x: x % 3 == 0, [1, 2, 3, 4, 5, 6, 9, 33]))
print(result)
