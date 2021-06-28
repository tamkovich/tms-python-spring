# Homework - 05
# task_5_6: Задан целочисленный массив. Определить количество участков массива, на котором
# элементы монотонно возрастают (каждое следующее число больше предыдущего). [02-4.1-ML27]
from random import randint

my_list = []
counter = 0
size_list = 20
for i in range(0, size_list):
    my_list.append(randint(1, 50))
print(f"Массив: {my_list}")
for i in range(1, size_list):
    if my_list[i] > my_list[i - 1]:
        counter += 1
print(f"Количество участков массива, на котором элементы возрастают: {counter}")
