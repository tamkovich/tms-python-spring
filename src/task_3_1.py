# Задание 3.1
# Введите число. Если это число делиться на 1000 без остатка,
# то выведите на экран "millennium"

num = input("Введите число: ")
if num.isdigit():
    num = int(num)
    if num % 1000 == 0:
        print("millennium")
else:
    print("Это не число!")
