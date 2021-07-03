# Homework - 07
# Задание 7.08: Написать функцию принимающая на вход неопределенным
# количеством аргументов и именованный аргумент mean_type.
# В зависимости от mean_type вернуть среднеарифметическое либо
# среднегеометрическое. Написать программу в виде трех функций.


def sr_ar(*args):
    return sum(args) / len(args)


def sr_geom(*args):
    pr = 1
    for i in args:
        pr *= i
    return pr ** (1 / len(args))


def moj_vyb(*args, mean_type=1):
    if mean_type == 1:
        print(f"Среднее арифметическое коллекции {coll} равно: {sr_ar(*args)}")
    elif mean_type == 2:
        print(f"Среднее геометрическое коллекции {coll} равно: {sr_geom(*args)}")
    else:
        print("Введите корректный тип операции: 1 - среднее арифметическое, 2 - среднее геометрическое!")


coll = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
moj_vyb(*coll, mean_type=1)
moj_vyb(*coll, mean_type=2)
moj_vyb(*coll, mean_type=5)
