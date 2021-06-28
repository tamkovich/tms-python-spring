# Homework - 05
# task_5_2: Дано число. Найти сумму и произведение его цифр.
sum_num = 0
pr_num = 1
number = int(input("Введите число: "))
for i in str(number):
    i = int(i)
    sum_num += i
    pr_num *= i
print(f"Сумма цифр числа: {sum_num}")
print(f"Произведение цифр числа: {pr_num}")
