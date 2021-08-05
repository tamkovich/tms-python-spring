"""Описать функцию Sin1( x , ε ) вещественного типа (параметры x , ε —
вещественные, ε > 0), находящую приближенное значение функции sin( x ):
sin( x ) = x – x ^3 /(3!) + x^ 5 /(5!) – ... + (–1) ^ n · x^( 2·n+1) /((2· n +1)!) + ... .
В сумме учитывать все слагаемые, модуль которых больше ε . С помощью
Sin1 найти приближенное значение синуса для данного x при шести данных
ε ."""


def fun_factorial(n: int) -> int:
    list_factorial = [i for i in range(1, n + 1)]
    factorial = 1
    for j in list_factorial:
        factorial *= j
    return factorial


def sin1(x: float, e: float) -> float:
    sin = x
    n = 1
    while True:
        sin_x_n = (-1) ** n * x ** (2 * n + 1) / (fun_factorial(2 * n + 1))
        if abs(sin_x_n) > e:
            sin += sin_x_n
        else:
            break
        n += 1
    return sin


if __name__ == "__main__":
    x = 7
    list_e = [1.0, 0.01, 0.001, 0.0001, 0.00001, 0.000001]
    for e in list_e:
        print(f'х = {x} ε = {e}" : sin1(x, e) = {sin1(x, e)}')
