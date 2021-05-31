# Задание 4_2
# Дан список целых чисел
# Подсчитать, сколько четных чисел в списке

# c while:
print('Вариант с while:')
list_1 = [1, 2, 3, 4, 9]
list_chet = []
a = 0
i = 0
b = 0
while i <= len(list_1) - 1:
    a = list_1[i]
    i += 1
    b += a
    if a % 2 == 0:
        list_chet.append(a)
print(f'Список чётных цифр - {list_chet}')
print(f'Количество чётных цифр = {len(list_chet)}')

# c for:
print('Вариант с for:')
list_chet = []
list_1 = [1, 2, 3, 4, 9]
for i in list_1:
    if i % 2 == 0:
        list_chet.append(i)
        i += 1
print(f'Список чётных цифр - {list_chet}')
print(f'Количество чётных цифр = {len(list_chet)}')
