num = input("Введите число: ")
if num.isdigit():
    num = int(num)
    if num % 1000 == 0:
        print("millennium")
else:
    print("Это не число!")