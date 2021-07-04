# Дана целочисленная квадратная матрица.
# Найти в каждой строке наи- больший элемент и поменять его местами с элементом главной диагонали.


from random import randint

matrix1 = []
n = int(input('Enter n:'))
m = int(input('Enter m:'))

matrix = [[randint(1, 9) for j in range(n)] for i in range(m)]
print(*matrix)
for i in range(min(n, m)):
    r = matrix[i].index(max(matrix[i]))
    matrix[i][i], matrix[i][r] = matrix[i][r], matrix[i][i]
print(*matrix)
