# Задание 5_6
# Задан целочисленный массив. Определить количество участков массива,
# на котором элементы монотонно возрастают
# (каждое число больше предыдущего)

from random import randint
list = []
x, check = 0, True
for i in range(1, 10):
    list.append(randint(1, 20))
print(list)
for j in range(1, len(list)):
    if list[j] > list[j-1]:
        if check == True:
            x += 1
            check = False
    else:
        check = True
print(f'количество участков, на которых элементы монотонно возрастают - {x}')
