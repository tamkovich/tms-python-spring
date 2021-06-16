# Homework - 03
# task_3_1: Введите число. Если это число делиться на 1000 без остатка, то выведите на
# экран "millennium".
number = input("Введите число: ")
if number.isdigit():
    if int(number) % 1000 == 0:
        print("millennium")
else:
    print("Введите целое число!")
