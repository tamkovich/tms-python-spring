"""1. Описать функцию fact2( n ), вычисляющую двойной факториал :n!! =
1·3·5·...·n, если n — нечетное; n!! = 2·4·6·...·n, если n — четное (n > 0 —
параметр целого типа. С помощью этой функции найти двойные
факториалы пяти данных целых чисел"""


c = [10, 8, 13, 16, 17]


def fact2(n):
    chet = 1
    nechet = 1
    for i in range(1, n + 1):
        if i % 2 == 0:
            chet = chet * i
        else:
            nechet *= i
    return chet, nechet


fact_c = [fact2(n) for n in c]
print(fact_c)
