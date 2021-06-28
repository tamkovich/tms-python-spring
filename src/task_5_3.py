# Homework - 05
# task_5_3: Два натуральных числа называют дружественными, если каждое из них
# равно сумме всех делителей другого, кроме самого этого числа. Найти все
# пары дружественных чисел, лежащих в диапазоне от 200 до 300. [02-3.2-HL02]
st_range = 200
end_range = 300
sravn_matr = {}
for i in range(st_range, end_range + 1):
    list_delit = []
    for j in range(1, i):
        if i % j == 0:
            list_delit.append(j)
    sum_delit = sum(list_delit)
    if st_range <= sum_delit <= end_range:
        sravn_matr[str(i)] = str(sum_delit)
#        print(f"{i}: {' '.join((map(str, list_delit)))}. Сумма делителей: {sum_delit}")
for key, value in sravn_matr.items():
    for key2, value2 in sravn_matr.items():
        if key == value2 and value == key2 and key != value:
            print(f"Дружественные числа: {key} {value}")
