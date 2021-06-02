#  Задан целочисленный массив. Определить количество участков массива,
# на котором элементы монотонно возрастают (каждое следующее число
# больше предыдущего)

from random import randint
from random import randrange
N = randint(1, 15)
print(N)
a = [randrange(1, 10) for i in range(N)]
print(a)
rez, point = 0, True
for i in range(1, N):
    if a[i - 1] < a[i]:
        if point:
            rez += 1
            point = False
    else:
        point = True
print("Count:", rez)
