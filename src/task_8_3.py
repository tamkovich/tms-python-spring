"""
Создать декоратор для функции, которая принимает список чисел.
Декоратор должен производить предварительную проверку данных -
удалять все четные элементы из списка
"""


def decorator_function(func):
    def wrapper(num_list):
        # Функция отфильтрует нечентные числа
        result = filter(lambda num: num % 2 != 0, num_list)
        func(list(result))
    return wrapper


@decorator_function
def list_of_word(num):
    # Вывод список нечетных чисел
    print(num)


n = [1, 5, 4, 7, 8, 12, 20]
list_of_word(n)
