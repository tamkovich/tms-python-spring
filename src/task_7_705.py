"""
Homework - 07
task_7_7.05: Создать функцию, принимающая на вход неопределенное
количество аргументом и возвращающая сумму args[i] * i
Пример: args = [4,3,2,1], 4 * 0 + 3 * 1 + 2 * 2 + 1 * 3 = 10
"""


def my_sum_func(*args: float) -> float:
    """Ф-ция возвращает сумму args[i] * i"""
    s = 0
    index = 0
    for i in args:
        s += i * index
        index += 1
    return s


if __name__ == "__main__":
    my_list = [1, 2, 1, 2, 1, 0.5]
    print(f'Сумма "args[i] * i" для {my_list} равна: {my_sum_func(*my_list)}')
