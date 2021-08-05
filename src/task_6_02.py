""" Дано число. Найти сумму и произведение его цифр. """
chislo = 2212345434334343874343874387438743
l = str(chislo)
k = len(list(l))
z = (list(l))
summa = 0
proizv = 1
i = 0
while True:
    if i < k:
        summa += int(z[i])
        proizv *= int(z[i])
        i += 1
    else:
        break
print(summa, proizv)
