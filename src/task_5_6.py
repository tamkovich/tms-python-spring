# """ Задан целочисленный массив. Определить количество участков массива,
# на котором элементы монотонно возрастают (каждое следующее число
# больше предыдущего)."""
import random
q = 0
mas = []
z = 0
a = 1
r = 0
while q < 19:
    rand = random.randint(1, 100)
    mas.append(rand)
    q += 1
print(mas)
while z < 18:
    if mas[z] < mas[a]:
        z += 1
        a += 1
        r += 1
    elif mas[z] == mas[a]:
        z += 1
        a += 1
        continue
    else:
        z += 1
        a += 1
    if a == 18:
        break
print(r)
