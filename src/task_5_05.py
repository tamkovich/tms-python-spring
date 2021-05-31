# Задание 5.5
# В массиве целых чисел с количеством элементов 19 определить максимальное
# число и заменить им все четные по значению элементы.

from random import randint

my_array = []
for i in range(19):
    my_array.append(randint(1, 100))
print(my_array)
max_num = my_array[0]
for num in my_array:
    if num > max_num:
        max_num = num
print(max_num)
for i in range(len(my_array)):
    if my_array[i] % 2 == 0:
        my_array[i] = max_num
print(my_array)
