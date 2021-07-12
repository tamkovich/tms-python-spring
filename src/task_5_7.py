# 7) Дана целочисленная квадратная матрица. Найти в каждой строке наибольший элемент и
# поменять его местами с элементом главной диагонали.[02-4.2-ML22]
import random
N = 3
matrix = []
for i in range(N):
    box = []
    for j in range(N):
        box.append(random.randint(1, 20))
    matrix.append(box)
print(matrix)
for i in range(N):
    a = matrix[i].index(max(matrix[i]))
    matrix[i][i], matrix[i][a] = matrix[i][a], matrix[i][i]
print(matrix)
