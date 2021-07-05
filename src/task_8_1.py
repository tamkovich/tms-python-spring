# Homework - 08
# task_8_1: Описать функцию fact2( n ), вычисляющую двойной факториал:
# n!! = 1·3·5·...·n, если n — нечетное; n!! = 2·4·6·...·n, если n — четное
# (n > 0 — параметр целого типа). С помощью этой функции найти двойные
# факториалы пяти данных целых чисел [01-11.2-Proc35]
from random import randint


def fact2(n: int) -> int:
    if n % 2 == 0:
        list_fact = [i for i in range(2, n + 1, 2)]
    else:
        list_fact = [i for i in range(1, n + 1, 2)]
    f = 1
    for i in list_fact:
        f *= i
    return f
    """Ф-ция формирует список четных или не четных значений, и далее по нему делает расчет"""


if __name__ == "__main__":
    rez_list = [randint(1, 9) for i in range(5)]
    for i in rez_list:
        print(f"Двойной факториал {i} равен: {fact2(i)}")
