# Задание 4_4
# Дан список
# Создать новый список, сдвинутый на 1 элемент влево
# Пример: 1 2 3 4 5 -> 2 3 4 5 1

# c while:
print('Вариант с while:')
list = [1, 2, 3, 4, 5, 6, 7]
i = 0
num = 0
while i < len(list) - 1:
    num = list.pop()
    list.insert(0, num)
    i += 1
print(list)

# c for:
print('Вариант с for:')
list = [1, 2, 3, 4, 5, 6, 7]
for i in range(len(list) - 1):
    num = list.pop()
    list.insert(0, num)
print(list)
