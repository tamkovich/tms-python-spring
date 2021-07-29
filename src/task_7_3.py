"""
Описать функцию Sin1( x , ε ) вещественного типа (параметры x , ε —
вещественные, ε > 0), находящую приближенное значение функции sin( x ):
sin( x ) = x – x ^3 /(3!) + x^ 5 /(5!) – ... + (–1) ^ n · x^( 2·n+1) /((2· n +1)!) + ... .
В сумме учитывать все слагаемые, модуль которых больше ε . С помощью
Sin1 найти приближенное значение синуса для данного x при шести данных

"""


def fact(n):
    f = 1
    for index in range(1, n + 1):
        f *= index
    return f


def Sin1(x: float, eps: float) -> float:
    n = 1
    res = x
    sin_x = 0
    while abs(res) > eps:
        sin_x += res
        n += 1
        res = (-1) ** n * (x ** (2 * n + 1)) / fact(2 * n + 1)
    return sin_x


eps = [0.1, 0.01, 0.001, 1, 1.01, 1.001]
x = 3.14 / 2
for i in eps:
    print(f"sin({round(x * 180 / 3.14)}, eps = {i}) = {round(Sin1(x, i), 4)}")
