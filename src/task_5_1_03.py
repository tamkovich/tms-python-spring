# Задача 5.3
# Два натуральных числа называют дружественными, если каждое из них
# равно сумме всех делителей другого, кроме самого этого числа. Найти все
# пары дружественных чисел, лежащих в диапазоне от 200 до 300. [02-3.2-HL02]

range_start, range_end = 200, 300
nums_and_sum = dict()

for number in range(range_start, range_end + 1):
    sum_of_divisors = 0
    for n in range(1, number):
        if number % n == 0:
            sum_of_divisors += n
    nums_and_sum.update({number: sum_of_divisors})

for number in nums_and_sum.keys():
    for friend in nums_and_sum.keys():
        if number != friend and (number == nums_and_sum[friend] and friend == nums_and_sum[number]):
            print(f"{number} is friendly to {friend}")
