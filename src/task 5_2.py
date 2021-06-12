# Задание 5_2
# Дано число. Найти сумму и произведение его цифр.

num = input('Введите число: ')
summ = 0
proizv = 1
list_num = list(num)
for i in list_num:
    summ += int(i)
    proizv *= int(i)
print(f'Сумма цифр вашего числа: {summ}')
print(f'Произведение цифр вашего числа: {proizv}')
