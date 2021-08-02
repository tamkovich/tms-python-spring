"""
Создать декоратор для функции, которая принимает список чисел.
Декоратор должен производить предварительную проверку данных -
удалять все четные элементы из списка.
"""
list_nums = []


def filter_nums(func):
    def wrapper(n: int):
        if n % 2 == 0:
            func(n)
    return wrapper


@filter_nums
def enter_nums(n: int):
    list_nums.append(n)
    print(list_nums)


while True:
    enter_nums(int(input('Enter a num: ')))
