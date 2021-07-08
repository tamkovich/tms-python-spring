"""
Homework - 09
task_9_3: Создать декоратор для функции, которая принимает список чисел.
Декоратор должен производить предварительную проверку данных -
удалять все четные элементы из списка.
"""
from random import randint


def del_even_num(real_func):
    def fake_func(*args: list) -> list:
        """Ф-ция проверяет четность списка list_num, формирует и возвращает список нечетных"""
        res = filter(lambda x: x % 2 != 0, real_func(*args))
        print(f"Список нечетных чисел: {list(res)}")
        return list(res)

    return fake_func


@del_even_num
def list_num(my_list: list) -> list:
    """Ф-ция принимает список чисел, принтит и возвращает их"""
    print(f"Первичный список чисел: {my_list}")
    return my_list


if __name__ == "__main__":
    list_num([randint(1, 10) for i in range(20)])
