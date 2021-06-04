# Задание 8.3
# Описать функцию Sin1( x , ε ) вещественного типа (параметры x , ε —
# вещественные, ε > 0), находящую приближенное значение функции sin( x ):
# sin( x ) = x – x ^3 /(3!) + x^ 5 /(5!) – ... + (–1) ^ n · x^( 2·n+1) /((2· n +1)!) + ... .
# В сумме учитывать все слагаемые, модуль которых больше ε . С помощью
# Sin1 найти приближенное значение синуса для данного x при шести данных
# ε .

def fact(num: int) -> int:
    return 1 if num == 0 else fact(num - 1) * num


def sin1(x: float, e: float) -> float:
    def summand(n: int) -> float:
        return x ** (2 * n - 1) * (-1) ** (n - 1) / fact(2 * n - 1)

    n = 1
    result = 0
    while True:
        term = summand(n)
        if abs(term) <= e:
            break
        else:
            result += term
            n += 1
    return result


ipsilons = [1, 0.1, 0.01, 0.001, 0.0001, 0.00001, 0.000001, 0.000000001]

ANGLE = 3.14 / 2  # pi/2 radians is equal to 90 degrees
for ipsilon in ipsilons:
    print(f"sin({round(ANGLE * 180 / 3.14, 0)}\u00b0) = {round(sin1(ANGLE, ipsilon), 7)}"
          f"   at \u03b5 = {ipsilon}")
