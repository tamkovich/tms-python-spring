# 4) Дан список. Создать новый список, сдвинутый на 1 элемент влево
# Пример: 1 2 3 4 5 ->  2 3 4 5 1
lst = [1, 2, 3, 4, 5]
new_lst = []
for i in lst:
    new_lst.insert(len(new_lst)-1, i)
print(new_lst)

lst_1 = [1, 2, 3, 4, 5]
new_lst_1 = []
k = 1
while k <= len(lst_1):
    new_lst_1.insert(len(new_lst_1)-1, k)
    k += 1
print(new_lst_1)
