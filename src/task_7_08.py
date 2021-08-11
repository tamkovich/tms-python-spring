"""Задание 7.08
Написать функцию принимающая на вход
неопределенным количеством аргументов и именованный
аргумент mean_type. В зависимости от mean_type вернуть
среднеарифметическое либо среднегеометрическое.
Написать программу в виде трех функций:
-среднеарифметическое
-среднегеометрическое
-точка входа"""
def sredn_arifm(*args):
    return sum(args) / len(args)


def sredn_geo(*args):
    proizv = 1
    for i in args:
        proizv = proizv * i
    return proizv ** (1 / len(args))


def enter_point(*args, mean_type=1):
    if mean_type == 1:
        return sredn_arifm(*args)
    else:
        return sredn_geo(*args)


lst = [1, 2, 20, 10]
lst_2 = [1, 2]
print(enter_point(*lst, mean_type=3))
print(enter_point(*lst_2, mean_type=1))
print(enter_point(*lst_2, mean_type=2))
