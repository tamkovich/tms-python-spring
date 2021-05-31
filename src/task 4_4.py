# Задание 4_4
# Дан список
# Создать новый список, сдвинутый на 1 элемент влево
# Пример: 1 2 3 4 5 -> 2 3 4 5 1

# while:
print('Вариант с while:')
list = [1, 2, 3, 4, 5, 6, 7]
list_new = []
i = 0
while i < len(list):
    num = list.pop()
    list_new.append(num)
print(list_new)

# for:
print('Вариант с for:')
list = [1, 2, 3, 4, 5, 6, 7]
list_new = []
for i in range(len(list)):
    num = list.pop()
    list_new.append(num)
print(list_new)
