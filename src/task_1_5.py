# Задача 1.5
# Даны катеты прямоугольного треугольника.
# Найти его гипотенузу и площадь

# Cathetuses of triangle
a = 10
b = 10

# Hypotenuse of triangle
hyp = (a ** 2 + b ** 2) ** 0.5

# Area of triangle
area = 0.5 * a * b

print(f'Cathetuses of triangle: a = {a}, b = {b}',
      f'Hypotenuse of triangle: {hyp}',
      f'Area of triangle: {area}', sep="\n")
