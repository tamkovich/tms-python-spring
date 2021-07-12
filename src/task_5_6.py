# 6) Задан целочисленный массив. Определить количество участков массива,
# на котором элементы монотонно возрастают (каждое следующее число
# больше предыдущего). [02-4.1-ML27]
import random

list = [random.randint(0, 20) for el in range(20)]
print(list)
k = 0
for i, el in enumerate(list):
    if i == len(list) - 1:
        break
    if list[i + 1] > el:
        print(str(list[i + 1]) + ' больше чем предыдущее ' + str(el))
        k += 1
        print(k)
