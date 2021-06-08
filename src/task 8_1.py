# Описать функцию fact2( n ), вычисляющую двойной факториал :n!! =
# 1·3·5·...·n, если n — нечетное; n!! = 2·4·6·...·n, если n — четное (n > 0 —
# параметр целого типа. С помощью этой функции найти двойные
# факториалы пяти данных целых чисел

list = [1, 2, 5, 6, 10]
def fact_2(n):
    for i in range(n + 1):
        if n % 2 != 0:
            if n == 1:
                return n
            else:
                return n * fact_2(n-2)
        elif n % 2 == 0:
            if n == 2:
                return n * 1
            else:
                return n * fact_2(n-2)

for n in list:
    print(fact_2(n))