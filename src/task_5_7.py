# """Дана целочисленная квадратная матрица. Найти в каждой строке наибольший
# элемент и поменять его местами с элементом главной диагонали"""
import random
matr = []
a = 0
box_2 = []
o = 0
for _ in range(1, 4):
    box = []
    for _ in range(1, 4):
        a = random.randint(1, 100)
        box.append(a)
    matr.append(box)
print(matr)
for i in matr:
    big_nam = 0
    for j in i:
        if j > big_nam:
            big_nam = j
    box_2.append(big_nam)
    a += 1
    i[o] = big_nam
    o += 1
print(box_2)
print(matr)
