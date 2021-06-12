# Два натуральных числа называют дружественными, если каждое из них
# равно сумме всех делителей другого, кроме самого этого числа. Найти
# все пары дружественных числе, лежащих в диапазоне от 200 до 300

for i in range(200, 301):
    summ_div_1, summ_div_2 = 0, 0
    for div_1 in range(1, i):
        if i % div_1 == 0:
            summ_div_1 += div_1
    for div_2 in range(1, summ_div_1):
        if summ_div_1 % div_2 == 0:
            summ_div_2 += div_2
    if i == summ_div_2 and i < summ_div_1:
        print(i, summ_div_1)
