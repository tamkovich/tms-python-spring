"""
Homework - 07
task_7_7.02: Написать программу для работы с матрицами:
              1. Создание
              2. Вывод
              3. Сумма всех элементов
              4. Нахождение максимального элемента
              5. Нахождение минимального элемента.
"""
from random import randint


def create_matrix(n: int, m: int) -> list:
    """Ф-ция создает матрицу n x m"""
    matrix = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(randint(1, 10))
        matrix.append(row)
    return matrix


def print_matrix(matrix: list) -> None:
    """Ф-ция выводит матрицу"""
    for row in matrix:
        print(row)


def sum_all_elements(matrix: list) -> int:
    """Ф-ция возвращает сумму всех элементов матрицы"""
    list_of_sum_elements = []
    for row in matrix:
        list_of_sum_elements.append(sum(row))
    return sum(list_of_sum_elements)


def find_max_element(matrix: list) -> int:
    """Ф-ция возвращает максимальный элемент матрицы"""
    list_of_max_elements = []
    for row in matrix:
        list_of_max_elements.append(max(row))
    return max(list_of_max_elements)


def find_min_element(matrix: list) -> int:
    """Ф-ция возвращает минимальный элемент матрицы"""
    list_of_min_elements = []
    for row in matrix:
        list_of_min_elements.append(min(row))
    return min(list_of_min_elements)


if __name__ == "__main__":
    my_matrix = create_matrix(4, 3)
    print_matrix(my_matrix)
    print(f"Сумма элементов матрицы: {sum_all_elements(my_matrix)}")
    print(f"Максимальный элемент матрицы: {find_max_element(my_matrix)}")
    print(f"Минимальный элемент матрицы: {find_min_element(my_matrix)}")
