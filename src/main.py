"""
Homework - 13
task_13_07:
Создать пакет следующей структуры:
src/
    matrix_utils/
        matrix_classes.py
        matrix_funcs.py
    main.py
Создать класс Matrix. Атрибуты - data(сама матрица - список списков), n, m.
Определить конструктор(с параметрами(размерность: n, m и случ.диапазон: a, b),
по-умолчанию (матрица 5 на 5 где все элементы равны нулю), копирования),
переопределить магический метод __str__ для красивого вывода.
Описать функции, которые принимают на вход объект класса Matrix.
Функции позволяют искать max элемент матрицы, min, сумму всех элементов.
Создать в файле main.py матрицу. Использоваться все описанными ф-ции и методы.
"""
from matrix_utils import matrix_classes
from matrix_utils import matrix_funcs


if __name__ == "__main__":
    matrix = matrix_classes.Matrix(1, 6, 3, 4)
    matrix.gen_default_matrix()
    print(matrix.data)
    matrix.data = matrix.gen_random_matrix()
    matrix.__str__()
    print(f"Максимальный элемент матрицы: {matrix_funcs.find_max_matrix_element(matrix)}")
    print(f"Минимальный элемент матрицы: {matrix_funcs.find_min_matrix_element(matrix)}")
    print(f"Сумма элементов матрицы: {matrix_funcs.find_sum_matrix_elements(matrix)}")
