"""  В массиве целых чисел с количеством элементов 19 определить максимальное
число и заменить им все четные по значению элементы. [02-4.1-BL19] """

import random
listik = []
for i in range(19):
    listik.append(random.randint(-100, 100))
max_is_listika = max(listik)
j = 0
k = 0
for j in listik:
    if j % 2 == 0:
        listik[k] = max_is_listika
    k += 1
print(listik)
