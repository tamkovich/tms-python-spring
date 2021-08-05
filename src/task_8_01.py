"""1. Описать функцию fact2( n ), вычисляющую двойной факториал :n!! =
1·3·5·...·n, если n — нечетное; n!! = 2·4·6·...·n, если n — четное (n > 0 —
параметр целого типа. С помощью этой функции найти двойные
факториалы пяти данных целых чисел [01-11.2-Proc35]"""


def fact_2(*args):
    for n in args:
        if n % 2 == 0:
            s = [number for number in range(2, n+1) if number % 2 == 0]
            fact_chet = 1
            for i in s:
                fact_chet *= i
            print(f"{n} = {fact_chet}")
        else:
            s = [number for number in range(1, n+1) if number % 2 != 0]
            fact_chet = 1
            for i in s:
                fact_chet *= i
            print(f"{n} = {fact_chet}")


numbers_ = [12, 13, 8, 1, 2]
for j in numbers_:
    fact_2(j)
