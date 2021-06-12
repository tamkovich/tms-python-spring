# Дана целочисленная квадратная матрица.
# Найти в каждой строке наибольший элемент и поменять его местами с элементом главной диагонали.

matrix = [[12, 23, 45, 56],
          [2, 9, 65, 55],
          [3, 6, 90, 5],
          [11, 12, 13, 14]]
n = len(matrix)

for i in range(n):
    index_max = matrix[i].index(max(matrix[i]))
    tmp = matrix[i][i]
    matrix[i][i] = matrix[i][index_max]
    matrix[i][index_max] = tmp

for line in matrix:
    print(line)
