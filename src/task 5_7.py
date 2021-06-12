# Задание 5_7
# Дана целочисленная квадратная матрица. Найти в каждой строке
# наибольший элемент и поменять его местами с элементом
# главной диагонали.

from random import randint
N = 3
M = 3
matrix = []
for i in range(N):
    box = []
    for j in range(M):
        box.append(randint(1, 20))
    matrix.append(box)
    print(box)
for i in range(N):
    a = matrix[i].index(max(matrix[i]))
    matrix[i][i], matrix[i][a] = matrix[i][a], matrix[i][i]
print(matrix)
