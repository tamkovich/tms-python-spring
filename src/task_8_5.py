# Дан список чисел. Найти произведение всех чисел, которые кратны 3.
from functools import reduce
filtr = filter(lambda x: x % 3 == 0, [1, 2, 3, 4, 15, 8, 9])
print(reduce(lambda p, x: p * x, filtr, 1))
