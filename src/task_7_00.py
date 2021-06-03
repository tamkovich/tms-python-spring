from random import randint


def create_matrix(n):
    matrix = []
    for i in range(n):
        box = []
        for j in range(n):
            box.append(randint(1, 20))
        matrix.append(box)
    return matrix


def print_matrix(matrix_):
    for line in matrix_:
        print(line)


def summ_all_elements(matrix_):
    summa_elements = []
    for line in matrix_:
        summa_elements.append(sum(line))
    return sum(summa_elements)


def max_of_all_elements(matrix_):
    max_element = []
    for line in matrix_:
        max_element.append(max(line))
    return max(max_element)


def min_of_all_elements(matrix_):
    min_element = []
    for line in matrix_:
        min_element.append(min(line))
    return min(min_element)


a = int(input(f"Введите размерность матрицы: "))
create_matrix(a)
matrix_ = create_matrix(a)
print_matrix(matrix_)
print(f"Сумма всех элементов: ", summ_all_elements(matrix_))
print(f"Максимальный элемент: ", max_of_all_elements(matrix_))
print(f"Минимальный элемент: ", min_of_all_elements(matrix_))
