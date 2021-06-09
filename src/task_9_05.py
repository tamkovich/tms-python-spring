"""Задание 9.05
Дан список чисел. Найти произведение всех
чисел, которые кратны 3."""

from functools import reduce
nambers = [1, 2, 3, 6, 9]
re = list(filter(lambda a: a % 3 == 0, nambers))
result = reduce(lambda b, x: b * x, re)
print(result)
