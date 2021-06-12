# В массиве целых чисел с количеством элементов 19 определить максимальное
# число и заменить им все четные по значению элементы.

from random import randrange
arr = [randrange(1, 100) for i in range(19)]
for i in range(0, len(arr)):
    if arr[i] % 2 == 0:
        arr[i] = max(arr)
print(arr)
