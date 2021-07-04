# Дано число. Найти сумму и произведение его цифр


number = input('число из двух чисел:')
number = str(number)
first_number = number[0]
second_number = number[1]
first_number = int(first_number)
second_number = int(second_number)
_sum = first_number + second_number
_mult = first_number * second_number
print(_sum, _mult)
