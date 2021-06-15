"""Дан список чисел. Найти произведение всех
чисел, которые кратны 3. """

from functools import reduce
list_num = [1, 2, 3, 4, 6, 7]
new_list = list(filter(lambda x: x % 3 == 0, list_num))
result = reduce(lambda current, new: current * new, new_list)
print(result)