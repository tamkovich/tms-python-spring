# 1) Дан список целых чисел.
# Создать новый список, каждый элемент которого равен исходному элементу
# умноженному на -2
lst = [1, 8, 34, 12]
new_lst = []
i = 0
for _ in lst:
    p = lst[i] * (-2)
    i += 1
    new_lst.append(p)
print(new_lst)

lst_1 = [1, 8, 34, 12]
new_lst_1 = []
k = 0
while k < len(lst_1):
    o = lst_1[k] * (-2)
    k += 1
    new_lst_1.append(o)
print(new_lst_1)

