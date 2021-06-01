# Дано число. Найти сумму и произведение его цифр.
n = input("Введите число: ")
if n.isdigit():
    summa = 0
    proizvedeniya = 1
    for j in n:
        summa += int(j)
        proizvedeniya *= int(j)
    print(f"Сумма цифр число {n} = {summa}")
    print(f"Произведения цифр число {n} = {proizvedeniya}")
