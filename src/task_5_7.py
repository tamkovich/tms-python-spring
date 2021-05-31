"""
Дана целочисленная квадратная матрица.
Найти в каждой строке наи- больший элемент и поменять его местами с элементом главной диагонали
"""
matrix = []
print("Введите размер квадратной матрицы: ")
n = input()
if n.isdigit():
    for i in range(int(n)):
        box = []
        for j in range(int(n)):
            print(f"Ввведите элемет [{i}][{j}]: ")
            x = int(input())
            box.append(x)
        matrix.append(box)
    print(matrix)
    for i in range(int(n)):
        max = matrix[i][0]
        for j in range(int(n)):
            if matrix[i][j] > max:
                max = matrix[i][j]
        matrix[i][i] = max
    print(matrix)
