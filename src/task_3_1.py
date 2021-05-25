# Введите число. Если это число делиться на 1000 без остатка, то выведите на экран "millennium"
number = int(input("Введите число:"))
if number % 1000 == 0:
    print("millennium")
