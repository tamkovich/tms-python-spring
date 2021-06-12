# """Для каждого натурального числа в промежутке от m до n вывести все делители,
# кроме единицы и самого числа. m и n вводятся с клавиатуры.
# Пример:m =100, n = 105"""
m = 100#input("start diapazon")
n = 105#input("finish diapazon")
ran = list(range(m, n + 1))
mas = []
dict_delit = {}
schet = 0
for i in ran:
    box = []
    for j in range(2, i):
        if j == i:
            break
        if i % j == 0:
            box.append(j)
    mas.append(box)
for t in ran:
    dict_delit[t] = mas[schet]
    schet += 1
print(mas)
print(dict_delit)
