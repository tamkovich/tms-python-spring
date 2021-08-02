"""
Написать функцию принимающая на вход неопределенным количеством аргументов и именованный аргумент mean_type.
В зависимости от mean_type вернуть среднеарифметическое либо среднегеометрическое. Написать программу
в виде трех функций:среднеарифметическое, среднегеометрическое, точка входа.
"""


def sredn_arifm(*args):
    """
    Данная функция вычисляет среднеарифметическое.
    """
    return sum(args) / len(args)


def sredn_geom(*args):
    """
    Данная функция вычисляет среднегеометрическое.
    """
    proizv = 1
    for i in args:
        proizv = proizv * i
    return proizv ** (1 / len(args))


def enter_point(*args, mean_type):
    """
    Данная функция проверяет является ли mean_type числом, если да , то срабатывает функция sredn_arifm.
    Если нет, то срабатывает функция sredn_geom.
    """
    if mean_type.isdigit():
        return sredn_arifm(*args)
    else:
        return sredn_geom(*args)


mean_type = '3'
print(enter_point(1, 2, 3, 6, mean_type=mean_type))
