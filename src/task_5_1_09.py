# Задание 5.09
# Для каждого натурального числа в промежутке от m до n вывести все делители,
# кроме единицы и самого числа. m и n вводятся с клавиатуры.
# Пример:m =100, n = 105
# 100: 2 4 5 10 20 25 50
# 101:
# 102: 2 3 6 17 34 51
# 103:
# 104: 2 4 8 13 26 52
# 105: 3 5 7 15 21 35

m = int(input("Enter the beginning of interval: "))
n = int(input("Enter the end of interval: "))

print(f"\nSearching the divisors for every number in [{m}...{n}] \n")

nums_and_divisors = []

for number in range(m, n + 1):
    divisors = []
    for divisor in range(2, number):
        if number % divisor == 0:
            divisors.append(divisor)
    nums_and_divisors.append({number: divisors})

for elem in nums_and_divisors:
    for num, divisors in elem.items():
        print(f"Divisors of {num}: {divisors}")
