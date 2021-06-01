# Homework - 01
# task_1_5: Даны катеты прямоугольного треугольника. Найти его гипотенузу и площадь.
import math

katet_1 = 5
katet_2 = 10
gipoten = math.sqrt(katet_1 ** 2 + katet_2 ** 2)
s_treug = katet_1 * katet_2 / 2
print(f"Гипотенуза треугольника = {gipoten}")
print(f"Площадь треугольника = {s_treug}")
