# Homework - 05
# task_5_5: В массиве целых чисел с количеством элементов 19 определить максимальное
# число и заменить им все четные по значению элементы. [02-4.1-BL19]
from random import randint

start_list = []
end_list = []
for i in range(0, 19):
    start_list.append(randint(1, 11))
print(f"Исходный список: {start_list}")
max_num = max(start_list)
print(f"Максимальное значение исходного списка: {max_num}")
for i in range(0, 19):
    if start_list[i] % 2 == 0:
        start_list[i] = max_num
print(f"Список после изменения: {start_list}")
