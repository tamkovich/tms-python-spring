# Задание 5_5
# В массиве целых числе с количеством элементов 19 определить
# максимальное число и заменить им все четные по значению элементы

from random import randint
list = []
for i in range(1, 20):
    list.append(randint(1, 101))
print(list)
a = 0
list_max = max(list)
for j in list:
    if j % 2 == 0:
        list[a] = list_max
    a += 1
print(list)
