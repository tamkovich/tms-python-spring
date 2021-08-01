"""6) Задан целочисленный массив. Определить количество участков массива,
на котором элементы монотонно возрастают (каждое следующее число
больше предыдущего)."""
import random
lst = [random.randint(0, 20) for el in range(20)]
print(lst)
k = 0
for i, el in enumerate(lst):
    if i == len(lst) - 1:
        break
    if lst[i + 1] > el:
        print(str(lst[i + 1]) + ' больше чем предыдущее ' + str(el))
        k += 1
        print(k)
