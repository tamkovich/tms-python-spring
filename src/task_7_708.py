"""
Homework - 07
task_7_7.08: Написать функцию принимающая на вход неопределенным
количеством аргументов и именованный аргумент mean_type.
В зависимости от mean_type вернуть среднеарифметическое либо
среднегеометрическое. Написать программу в виде трех функций.
"""


def sr_ar(*args: int) -> float:
    """Ф-ция возвращает среднеарифметическое"""
    return sum(args) / len(args)


def sr_geom(*args: int) -> float:
    """Ф-ция возвращает среднегеометрическое"""
    pr = 1
    for i in args:
        pr *= i
    return pr ** (1 / len(args))


def moj_vyb(*args: int, mean_type=1) -> None:
    """Ф-ция принимает mean_type и запускает sr_ar или sr_geom соответственно"""
    if mean_type == 1:
        print(f"Среднее арифметическое коллекции {coll} равно: {sr_ar(*args)}")
    elif mean_type == 2:
        print(f"Среднее геометрическое коллекции {coll} равно: {sr_geom(*args)}")
    else:
        print("Введите корректный тип операции: 1 - ср.арифметическое, 2 - ср.геометрическое!")


if __name__ == "__main__":
    coll = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    moj_vyb(*coll, mean_type=1)
    moj_vyb(*coll, mean_type=2)
    moj_vyb(*coll, mean_type=5)
