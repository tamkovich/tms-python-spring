# Задание 5.2:
# Дано число. Найти сумму и произведение его цифр.

summa = 0
mult = 1
num = input("Введите число: ")
for i in num:
    summa += int(i)
    mult *= int(i)
print("Сумма цифр числа: ", summa)
print("Произведение цифр числа: ", mult)
