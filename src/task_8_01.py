# Описать функцию fact2( n ), вычисляющую двойной факториал :n!! =
# 1·3·5·...·n, если n — нечетное; n!! = 2·4·6·...·n, если n — четное (n > 0 —
# параметр целого типа. С помощью этой функции найти двойные
# факториалы пяти данных целых чисел

from functions import double_recurs_factorial
num_list = [1, 2, 3, 4, 5]
print(f'Factorials\n{num_list}\n |  |  |  |  |\n'
      f'{[double_recurs_factorial(n) for n in num_list]}')
