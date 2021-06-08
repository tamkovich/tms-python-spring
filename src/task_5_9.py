# Для каждого натурального числа в промежутке от m до n вывести все делители,
# кроме единицы и самого числа. m и n вводятся с клавиатуры.
# Пример:m =100, n = 105

m = int(input('Enter start number: '))
n = int(input('Enter end number: '))


def divisor(number):
    divisors = ''
    for i in range(2, number):
        if number % i == 0:
            divisors += str(i) + ' '
    return divisors


for i in range(m, n + 1):
    result = str(i) + ': ' + str(divisor(i))
    print(result)
