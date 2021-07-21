"""
Homework - 09
task_9_4: Создать универсальный декоратор, который меняет порядок аргументов в
функции на противоположный.
"""


def revers_param(real_func):
    def fake_func(*args: int) -> int:
        """Ф-ция разворачивает параметры входной ф-ции"""
        return real_func(*args[::-1])

    return fake_func


@revers_param
def test_calcul(a, b, c: int) -> int:
    """Ф-ция делает тестовый расчет"""
    res = (a + b) * c
    print(f"Расчет по обратному порядку аргументов ({a} + {b}) * {c}: {res}")
    return res


if __name__ == "__main__":
    print(f"Расчет по прямому порядку аргументов (2 + 3) * 5: {(2 + 3) * 5}")
    test_calcul(2, 3, 5)
