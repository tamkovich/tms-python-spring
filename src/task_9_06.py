"""
Задание 9.6:
Написать декоратор, который будет выводить время выполнения функции
"""

from datetime import datetime


def time_checker(real_func):  # Создаем декоратор как функцию высшего порядка
    def fake_func(*args):  # Создаем функцию-обёртку, которая будет подсчитывать время выполнения основной функции
        time_start = datetime.now()  # Добавляем время начала выполнения функции в переменную
        real_func(*args)  # Запускаем функцию
        time_end = datetime.now()  # Добавляем время окончания выполнения функции в переменную
        run_time = time_end - time_start  # Считаем время выполнения функции
        print(f"Время выполнения функции: {run_time.microseconds} миллисекунд")

    return fake_func


@time_checker
def test_function():
    """
    Данная функция проходит по списку и выводит имена в которых есть буква k
    """
    names = ["Ihar", "Zheka", "Kostya", "Petr", "Nikolai"]
    names_with_k = filter(lambda name: "k" in name.lower(), names)
    print(list(names_with_k))


test_function()
