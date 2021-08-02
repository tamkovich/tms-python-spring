"""
В массиве целых чисел с количеством элементов 19 определить максимальное
число и заменить им все четные по значению элементы. [02-4.1-BL19]
"""
from random import random
N = 19
arr = [0] * 19
even = []
for i in range(N):
    arr[i] = int(random() * 100)
    if arr[i] % 2 == 0:
        even.append(i)
print(arr)
k = max(arr)
print(k)
for j in even:
    arr[j] = k
print(arr)
