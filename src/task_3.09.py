# Вычислить квадратное уравнение ax2 + bx + c = 0 (*)
# D = b2 – 4ac;
# x1,2 = (-b +/- sqrt (D)) / 2a
# Предусмотреть 3 варианта:
# 1) Два действительных корня
# 2) Один действительный корень
# 3) Нет действительных корней

from math import sqrt
a, b, c = float(input('Value a: ')), float(input('Value b: ')), float(input('Value c: '))
D = b ** 2 - 4 * a * c
if D > 0:
    x1 = (-b + sqrt(D)) / (2 * a)
    x2 = (-b - sqrt(D)) / (2 * a)
    print("Discriminant =", D, "\nx1 =", x1, "\nx2 =", x2)
elif D == 0:
    x = (-b / (2 * a))
    print("Discriminant =", int(D), "\nx =", x)
else:
    print("Discriminant =", D, "\nThis equation hasn't solutions")
