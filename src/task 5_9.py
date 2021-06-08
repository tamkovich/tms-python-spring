# Задание 5_9
# Для каждого натурального числа в промежутке от m до n
# вывести все делители кроме единицы и самого числа.
# m и n вводятся с клавиатуры

m = input('Введите число m: ')
n = input('Введите число n: ')
m = int(m)
n = int(n)
x = 0
list_1 = []
for i in range(m, n + 1):
    box = []
    for d in range(2, i):
        if i % d == 0:
            box.append(str(d))
    list_1.append(box)
    a = ', '.join(list_1[x])
    if len(a) < 1:
        print(f'Число {i} - не имеет делителей')
    else:
        print(f'Делители числа {i}: {a}')
    x += 1
