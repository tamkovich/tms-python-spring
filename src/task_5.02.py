# Дано число. Найти сумму и произведение его цифр.

x = input()
list_x, summ, mul = list(x), 0, 1
for i in list_x:
    summ += int(i)
    mul *= int(i)
print(summ, mul)
