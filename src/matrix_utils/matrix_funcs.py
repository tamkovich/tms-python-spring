from matrix_utils import matrix_classes
# PyCharm ругает строку (Unresolved reference 'matrix_utils' и 'matrix_classes'), но без нее не работает.


def find_max_matrix_element(my_matrix: matrix_classes.Matrix) -> int or float:
    """ Ф-ция находит max элемент во входящем объекте класса Matrix"""
    list_max = []
    for i in my_matrix.data:
        list_max.append(max(i))
    max_num = max(list_max)
    return max_num


def find_min_matrix_element(my_matrix: matrix_classes.Matrix) -> int or float:
    """ Ф-ция находит min элемент во входящем объекте класса Matrix"""
    list_min = []
    for i in my_matrix.data:
        list_min.append(min(i))
    min_num = min(list_min)
    return min_num


def find_sum_matrix_elements(my_matrix: matrix_classes.Matrix) -> int or float:
    """ Ф-ция находит сумму элементов входящего объекта класса Matrix"""
    list_sum = []
    for i in my_matrix.data:
        list_sum.append(sum(i))
    sum_num = sum(list_sum)
    return sum_num
