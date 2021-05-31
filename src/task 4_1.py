# Задание 4_1
# Дан список целых чисел
# Создать новый список, каждый элемент которого равен исходному элементу умноженному на -2

# while:
print('Вариант с while:')
list_1 = [1, 2, 4, 5]
list_new = []
c = 0
a = -2
b = 0
while True:
    if b <= len(list_1) - 1:
        c = a * list_1[b]
        b += 1
        list_new.append(c)
    else:
        break
print(list_new)

# for:
print('Вариант с for:')
list_new = []
list_1 = [1, 2, 4, 5]
for i in list_1:
    a = -2
    c = a * i
    list_new.append(c)
print(list_new)
