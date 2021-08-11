"""Задание 7.02 (HW)
Написать программу для работы с матрицами:"""
"""1)Создание"""


import random


def create_matrix(n):
    matrix = []
    for i in range(n):
        box = []
        for j in range(n):
            box.append(random.randint(1, 20))
        matrix.append(box)
    print(matrix)
    return matrix


"""2) Вывод"""


def print_matrix(matrix):
    for row in matrix:
        print(row)


"""3)Сумма всех элементов"""


def sum_all_elements(matrix):
    list_of_all_elements = []
    for row in matrix:
        list_of_all_elements.append(sum(row))
    return sum(list_of_all_elements)

"""4)Нахождение максимального элемента"""


def find_max_element(matrix):
    list_of_max_elements = []
    for row in matrix:
        list_of_max_elements.append(max(row))
    return max(list_of_max_elements)

"""5)Нахождение минимального элемента"""


def find_min_element(matrix):
    list_of_min_elements = []
    for row in matrix:
        list_of_min_elements.append(min(row))
    return min(list_of_min_elements)


matrix = create_matrix(3)
print_matrix(matrix)
print("Sum of all elements:", sum_all_elements(matrix))
print("Max element:", find_max_element(matrix))
print("Min element:", find_min_element(matrix))
