# 4) Дан список. Создать новый список, сдвинутый на 1 элемент влево
# Пример: 1 2 3 4 5 ->  2 3 4 5 1
list = [1, 2, 3, 4, 5]
new_list = []
for i in list:
    new_list.insert(len(new_list)-1, i)
print(new_list)

list_1 = [1, 2, 3, 4, 5]
new_list_1 = []
k = 1
while k <= len(list_1):
    new_list_1.insert(len(new_list_1)-1, k)
    k += 1
print(new_list_1)
