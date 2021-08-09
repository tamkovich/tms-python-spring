"""
Создать матрицу
"""
def create_matrix(n1, m1):
    array = []
    for i in range(n1):
        box = []
        for j in range(m1):
            print(f"Ввведите элемет [{i}][{j}]: ")
            x = int(input())
            box.append(x)
        array.append(box)
    return array


"""
Вывод матрицы
"""
def print_matrix(array):
    for row in array:
        print(row)
        # вывод строки матрицы


"""
Нахождения максимального элемента
"""
def find_max_element(array):
    list_of_max_elements = []
    # создаеем список максимальных элементов из каждой строки
    for row in array:
        list_of_max_elements.append(max(row))
        # добавление максимального элемента из строки
    return max(list_of_max_elements)


"""
Нахождения минимального элемента
"""
def find_min_element(array):
    list_of_max_elements = []
    for row in array:
        list_of_max_elements.append(min(row))
        # добавление минимального элемента из строки
    return min(list_of_max_elements)


"""
Нахождения сумму элементов
"""
def sum_all_elements(array):
    """

    создаеем список сумм каждой строки
    """
    list_of_max_elements = []
    for row in array:
        list_of_max_elements.append(sum(row))
        """
        добавление суммы всех элементов строки в список
        """
    return sum(list_of_max_elements)


while True:
    print("1. Создать матрицу")
    print("2. Вывод матрицы")
    print("3. Найти максимальный элемент в матрице")
    print("4. Найти минимальный элемент в матрице")
    print("5. Найти сумму элементов матрицы")
    num = input()
    if num.isdigit():
        if int(num) == 1:
            print("Введите размер матрица n, m:")
            n = int(input())
            m = int(input())
            matrix = [n, m]
            # noinspection PyRedeclaration
            matrix = (create_matrix(n, m))
        if int(num) == 2:
            # noinspection PyUnboundLocalVariable
            print_matrix(matrix)
        if int(num) == 3:
            print(f"Максимальный элемент: {find_max_element(matrix)}")
        if int(num) == 4:
            print(f"Минимальный элемент: {find_min_element(matrix)}")
        if int(num) == 5:
            print(f"Сумма элементов матриса: {sum_all_elements(matrix)}")
        print("Для выхода из программы нажмите '0', для продолжени нажмите на enter")
        num = input()
        if num.isdigit():
            if int(num) == 0:
                break
