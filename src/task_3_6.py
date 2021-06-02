a = int(input())
b = int(input())
c = int(input())
d = b ** 2 - 4 * a * c
if d > 0:
    x_1 = (-b + d ** 0.5) / 2 * a
    x_2 = (-b - d ** 0.5) / 2 * a
    print(x_1, 'и', x_2, 'два действительныйх корня.')
elif d == 0:
    x = -b / 2 * a
    print(x, 'один действительный корень')
else:
    print('Нет дествительныйх корней')
