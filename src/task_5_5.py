"""
В массиве целых чисел с количеством элементов 19
определить максимальное число и заменить им все четные по значению элементы.
"""
mas = []
print("Введите элемент массива: ")
for i in range(19):
    print(f"{i} - й элемент: ")
    x = int(input())
    mas.insert(i, x)
print(mas)
max = mas[0]
for i in range(19):
    if mas[i] > max:
        max = mas[i]
print("Максимальный элемент в массиве равен: ", max)
for i in range(19):
    if mas[i] % 2 == 0:
        mas[i] = max
print(mas)