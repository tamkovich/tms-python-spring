# Дана целочисленная квадратная матрица. Найти в каждой строке
# наибольший элемент и поменять его местами с элементом главной диагонали

from random import randint
n = 2
matrix = [[randint(1, 9) for j in range(n)] for i in range(n)]
print(matrix)
for i in range(n):
    r = matrix[i].index(max(matrix[i]))
    matrix[i][i], matrix[i][r] = matrix[i][r], matrix[i][i]
print(matrix)
