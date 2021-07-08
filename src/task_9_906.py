"""
Homework - 09
task_9_906: Написать декоратор, который будет выводить время выполнения функции
# from datetime import datetime
# time = datetime.now()
"""
import time
from datetime import datetime


def time_checker(real_func):
    def fake_func(*args):
        """Измерение времени выполнения ф-ции (+end) с задержкой (искл.рез. 0.0с)"""
        start = time.time()
        time.sleep(0.2)
        real_func(*args)
        end = time.time()
        print(f'Функция выполняется за: {end - start - 0.2} секунд.')

    return fake_func


@time_checker
def time_func():
    """Декоратор применен к ф-ции вывода и возвращения текущей даты и времени"""
    print(f'"Сейчас" - это: {datetime.now()}.')
    return datetime.now()


if __name__ == "__main__":
    time_func()
