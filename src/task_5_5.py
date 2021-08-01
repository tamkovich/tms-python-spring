"""5) В массиве целых чисел с количеством элементов 19 определить максимальное
число и заменить им все четные по значению элементы."""
from random import randint
list = []
a = 0
while a <= 19:
    list.append(randint(0, 50))
    a += 1
print(list)
print(max(list))
max_list = max(list)
k = 0
for i in list:
    if i % 2 == 0:
        list[k] = max_list
    k += 1
print(list)
