# Homework - 05
# task_5_7: Дана целочисленная квадратная матрица. Найти в каждой строке наибольший
# элемент и поменять его местами с элементом главной диагонали. [02-4.2-ML22]
from random import randint

n = m = int(input("Введите размер квадратной матрицы: "))
matrix = []
for a in range(0, n):
    list_matr = []
    for b in range(0, n):
        list_matr.append(randint(1, 111))
    matrix.append(list_matr)
print(f"Исходная матрица: {matrix}")
gl_diag = 0
for i in matrix:
    max_num = max(i)
    num_gl_diag = i[gl_diag]
    for j, elem in enumerate(i, 0):
        if elem == max_num:
            i[j] = num_gl_diag
    i[gl_diag] = max_num
    gl_diag += 1
print(f"Матрица после изменения: {matrix}")
