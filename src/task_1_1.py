import math

# Задание 1
a = 5
b = 2
summa = a + b
div = a / b
mult = a * b
print("Сумма равна:", summa)
print("Разность равна:", div)
print("Произведение равно:", mult)

# Задание 2 Сделал так, потому что через input постоянно просило вводить числа
x = 6
y = -8
result = (math.fabs(x) - math.fabs(y)) / (1 - math.fabs(x * y))
print("Result is: ", result)

# Задание 3
L = 3
S = math.pow(L, 2)
V = math.pow(L, 3)
print("Square:", S)
print("Volume:", V)

# Задание 4
num_1 = 6
num_2 = 7
arith = (num_1 + num_2) / 2
geom = math.sqrt(num_1 * num_2)
print("Average:", arith)
print("Geometric mean:", geom)

# Задание 5
a = 6
b = 10
c = math.sqrt(math.pow(a, 2) + math.pow(b, 2))
s = a * b / 2
print("Hypotenuse:", c)
print("Square:", s)
