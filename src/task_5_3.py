# Два натуральных числа называют дружественными, если каждое из
# них равно сумме всех делителей другого, кроме самого этого числа.
# Найти все пары дружественных чисел, лежащих в диапазоне от 200 до 300.


def get_divisors_sum(_num):
    divisors_sum = 0
    for divisor in range(1, _num):
        if _num % divisor == 0:
            divisors_sum += divisor
    return divisors_sum


number_list = []
for _num in range(200, 300 + 1):
    if _num not in number_list:
        _divisors_sum = get_divisors_sum(_num)
        if 200 < _divisors_sum < 300 and \
                _num != _divisors_sum and _num == get_divisors_sum(_divisors_sum):
            number_list.append(_divisors_sum)
            print(_num, _divisors_sum)
