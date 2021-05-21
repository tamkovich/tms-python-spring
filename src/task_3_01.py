# Задание 3.01
# Введите число. Если это число делиться на 1000 без остатка, то выведите на
# экран "millennium"

num = input("Input integer:")

if num.isdigit():
    num = int(num)
    if num % 1000 == 0:
        print("millennium")
else:
    print("This is not integer!")
