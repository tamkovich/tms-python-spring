""" Задание 8.1
Описать функцию fact2( n ), вычисляющую двойной факториал :n!! =
1·3·5·...·n, если n — нечетное; n!! = 2·4·6·...·n, если n — четное (n > 0 —
параметр целого типа. С помощью этой функции найти двойные
факториалы пяти данных целых чисел"""


def fact2(n: int) -> int:
    start = 2 if n % 2 == 0 else 1
    fact = start
    for next_ in range(start + 2, n + 1, 2):
        fact *= next_
    return fact


nums = [1, 4, 7, 10, 15]
for num in nums:
    print(f"{num}!! = {fact2(num)}")
