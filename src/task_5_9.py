"""
Для каждого натурального числа в промежутке от m до n вывести все делители,
кроме единицы и самого числа. m и n вводятся с клавиатуры
"""
print("Введите число n = ", end=' ')
n = input()
print("Введите число m = ", end=' ')
m = input()
if n < m and n.isdigit() and m.isdigit():
    while int(n) <= int(m):
        i = 2
        print(f"\nДелители числа {n}: ", end=' ')
        while i < int(n):
            if int(n) % i == 0:
                print(i, end=' ')
            i += 1
            n = int(n)
        n += 1
