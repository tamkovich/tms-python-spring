# """В массиве целых чисел с количеством элементов 19 определить максимальное
# число и заменить им все четные по значению элементы"""
import random
q = 0
mas = []
big_namb = 0
r = 0
while q < 19:
    rand = random.randint(1, 100)
    mas.append(rand)
    q += 1
big_namb = mas[0]
for i in range(1, len(mas)):
    if mas[i] > big_namb:
        big_namb = mas[i]
while r < len(mas):
    if mas[r] % 2 == 0:
        mas[r] = big_namb
    r += 1
print(big_namb)
print(mas)