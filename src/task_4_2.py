# 2) Дан список целых чисел. Подсчитать сколько четных чисел в списке
lst = [2, 8, 34, 12, 432, 67897]
s = 0
for value in lst:
    if value % 2 == 0:
        s += 1
print(s)

list_1 = [2, 8, 34, 12, 432, 67897]
ch = 0
k = 0
while k < len(list_1):
    ch += (list_1[k] + 1) % 2
    k += 1
print(ch)
