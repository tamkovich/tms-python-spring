""" Дана целочисленная квадратная матрица. Найти в каждой строке наи-
больший элемент и поменять его местами с элементом главной диагонали.
[02-4.2-ML22] """

A = [[11, 2, 30, 4],
     [10, 12, 3, 40],
     [1, 20, 13, 4],
     [1, 20, 3, 14],
     ]
z = 0
for i in A:
    naibolshii_element_v_stroke = max(i)
    print(naibolshii_element_v_stroke)
    element_glavnoi_diagonali = i[z]
    for j, elem in enumerate(i):
        if elem == naibolshii_element_v_stroke:
            i[j] = element_glavnoi_diagonali
        i[z] = naibolshii_element_v_stroke
    z += 1
print(A)
