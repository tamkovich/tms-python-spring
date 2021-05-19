# Задача 1.4
# Даны два действительных числа.
# Найти среднее арифметическое и среднее геометрическое этих чисел

x1 = 3
x2 = 7

average = (x1 + x2) / 2  # Arithmetic average
average_geom = (x1 * x2) ** 0.5  # Geometric average

print(f'X1 = {x1}, X2 = {x2}',
      f'Arithmetic average of X1 and X2: {average}',
      f'Geometric average of X1 and X2: {average_geom}', sep="\n")
