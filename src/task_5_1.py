while True:
    print(f"введине X", end=" ")
    X = int(input())
    while True:
        print(f"введине Y", end=" ")
        Y = int(input())
        print(f"введине знак операции", end=" ")
        sign = input()
        if Y == 0 and sign == "/":
            print("вы вели не правильный Y на ноль делить нельзя")
            continue
        elif sign == "/" or sign == "*" or sign == "+" or sign == "-":
            break
        elif sign == "0":
            print("завершение работы програмы")
            exit()

        else:
            print("вы вели не правильный знак")

    if sign == "+":
        Z = X + Y
        write = "сумма равна"
    elif sign == "-":
        Z = X - Y
        write = "разность равна"
    elif sign == "*":
        Z = X * Y
        write = "произведение равно"
    elif sign == "/":
        Z = X / Y
        write = "частное равно"

    print(f"{write}, {Z}")
