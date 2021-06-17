"""Создать декоратор для функции, которая принимает список чисел.
Декоратор должен производить предварительную проверку данных -
удалять все четные элементы из списка."""

def decor_f(func):
    def wrapper(*args):
        list_result = list(filter(lambda i: i % 2 != 0, args))
        func(list_result)
    return wrapper

@ decor_f
def list_num(num):
    print(num)

list_num(1, 2, 3)
