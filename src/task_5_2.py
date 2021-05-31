# Дано число. Найти сумму и произведение его цифр.
n = input("Введите число: ")
if n.isdigit():
    summa = 0
    proizvedeniya = 1
    for i in range(len(n)):
        summa += int(n[i])
        proizvedeniya *= int(n[i])
    print(f"Сумма цифр число {n} = {summa}")
    print(f"Произведения цифр число {n} = {proizvedeniya}")
