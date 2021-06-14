"""
Задан целочисленный массив.
Определить количество участков массива,
на котором элементы монотонно возрастают
"""
mas = []
k = 0
print("Введите размер массива: ")
n = input()
if n.isdigit():
    for i in range(int(n)):
        print(f"{i} - й элемент: ")
        x = int(input())
        mas.insert(i, x)
    print(mas)
    i = 0
    while i < len(mas) - 1:
        f = 0
        while mas[i] < mas[i + 1]:
            i += 1
            f = 1
        if f == 1:
            k += 1
        i += 1
    print("Количество участок в массиве, где элементы возрастают: ", k)
