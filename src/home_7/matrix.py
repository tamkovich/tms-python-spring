import random


def create_matrix(width=5, height=5, range_from=0, range_to=10):
    array = []
    for i in range(height):
        array.append([])
        for _ in range(i * width, width * (i + 1)):
            array[i].append(random.randint(range_from, range_to))
    return array


def print_matrix(matrix):
    for row in matrix:
        print(row)


def find_max_element(matrix):
    list_of_max_elements = []
    for row in matrix:
        list_of_max_elements.append(max(row))
    return max(list_of_max_elements)


def find_min_element(matrix):
    list_of_max_elements = []
    for row in matrix:
        list_of_max_elements.append(min(row))
    return min(list_of_max_elements)


def sum_all_elements(matrix):
    list_of_sum_all_rows = []
    for row in matrix:
        list_of_sum_all_rows.append(sum(row))
    return sum(list_of_sum_all_rows)


matrix = create_matrix(7, 10, 30, 200)

print_matrix(matrix)
print(find_max_element(matrix))
print(find_min_element(matrix))
print(sum_all_elements(matrix))
