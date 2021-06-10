# Дан список чисел. Найти произведение всех чисел, которые кратны 3.
from functools import reduce
print(reduce(lambda p, x: p * x, [1, 2, 3, 4, 15, 8, 9], 1))
