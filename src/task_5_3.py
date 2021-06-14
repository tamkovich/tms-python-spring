"""
Два натуральных числа называют дружественными,
если каждое из них равно сумме всех делителей другого,
кроме самого этого числа. Найти все пары дружественных чисел,
лежащих в диапазоне от 200 до 300.
"""
number = 200
sum_second = 0
while number <= 300:
    sum_first = 0
    i = 1
    while i < number:
        if number % i == 0:
            sum_first += i
        i += 1
    j = number + 1
    while j <= 300:
        index = 1
        while index < j:
            if j % index == 0:
                sum_second += index
            index += 1
        if sum_first == j and sum_second == number:
            print(f"{number} и {j} являються дружественными числами")
        sum_second = 0
        j += 1
    number += 1
