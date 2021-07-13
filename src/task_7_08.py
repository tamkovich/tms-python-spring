"""Задание 7.08
Написать функцию принимающая на вход
неопределенным количеством аргументов и именованный
аргумент mean_type. В зависимости от mean_type вернуть
среднеарифметическое либо среднегеометрическое.
Написать программу в виде трех функций"""


def ar_geo(*args, mean_type=0):
    if mean_type == 0:
        return sr_arefm(*args)
    if mean_type == 1:
        return sr_geometr(*args)


def sr_arefm(*args):
    arg_sum = 0
    schetchik = 0
    sr_arefm = 0
    for i in args:
        arg_sum += i
        schetchik += 1
    sr_arefm = arg_sum / schetchik
    return sr_arefm


def sr_geometr(*args):
    arg_proizv = 1
    sr_geometr = 0
    schetchik = 0
    for i in args:
        arg_proizv *= i
        schetchik += 1
    sr_geometr = arg_proizv ** (1 / schetchik)
    return sr_geometr


print(ar_geo(5, 6, 4, mean_type=1))
