from math import fabs
from math import sqrt
## Первое задание
a = 4.6
b = 13.7
summa = a + b
difference = b - a
product_numbers = a*b
print(f"сумма чисел равна {summa}, разность равно {difference}, произведение равно {product_numbers}")
## Второе задание используем функцию fabs для модуля числа
x = -4.5
y = 9.7
composition = (fabs(x) - fabs(y))/(1 + fabs(x*y))
print(composition)
## Третье задание по нахождению пощади и объема
length = 4
square = length**2
size = length**3
print(f"площадь стороны равна {square}, объем куба равна {size}")

## Четвертое задание на среднее арифметическое и геометрическое
last = (1,2,5,8,1,5,2,6,3)
arithmetical_mean = sum(last)/len(last)
product_numbers_1 = 1
for i in range(len(last)):
    product_numbers_1 = 1 * last[i] * product_numbers_1


Geometric_Mean = product_numbers_1/len(last)

print(f"среднее арифметическое равно {int(arithmetical_mean)} , среднее геометрическое равно {Geometric_Mean}")

## Пятое задание на нахождение гипотнузы и площади
katet_1 = 5
katet_2 = 8
gipotenuza = sqrt(katet_1**2 + katet_2**2)
square_treugolnika = katet_1*katet_2/2
print(f"гипотенуза равна {gipotenuza}, пощадь равна {square_treugolnika}")