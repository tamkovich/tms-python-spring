# Задание 5.5
# В массиве целых чисел с количеством элементов 19 определить максимальное
# число и заменить им все четные по значению элементы. [02-4.1-BL19]

from random import randint

src_list = []
list_size = 19

for i in range(list_size):  # src_list = [randint(1, 500) for i in range(list_size)]
    src_list.append(randint(1, 500))
print(f"Source array:\n{src_list}\n")

max_elem = src_list[0]
for elem in src_list:
    if elem > max_elem:
        max_elem = elem

print(f"Max element in source array: {max_elem}\n")

for index, elem in enumerate(src_list):
    if elem % 2 == 0:
        src_list[index] = max_elem

print(f"The source array where even elements replaced with max = {max_elem}:\n{src_list}")
