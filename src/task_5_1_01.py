# Задание 5.1
# Написать программу, в которой вводятся два операнда Х и Y и знак операции
# sign (+, –, /, *). Вычислить результат Z в зависимости от знака. Предусмотреть
# реакции на возможный неверный знак операции, а также на ввод Y=0 при
# делении. Организовать возможность многократных вычислений без перезагрузки
# программа (т.е. построить бесконечный цикл). В качестве символа прекращения
# вычислений принять ‘0’ (т.е. sign='0').

SIGN_SET = {"+", "–", "/", "*", "0"}
need_works = True

while need_works:
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))

    correct_sign = False
    while not correct_sign:
        sign = input("Enter operation type (+, –, /, *) or 0 for exit: ")
        correct_sign = sign in SIGN_SET

    if sign == "0":
        need_works = False
        print("Exit program.")
    elif sign == "/":
        if y != 0:
            result = x / y
            print(f"{x} {sign} {y} = {result}")
        else:
            print("It's impossible to divide by zero.")
    elif sign == "*":
        result = x * y
        print(f"{x} {sign} {y} = {result}")
    elif sign == "+":
        result = x + y
        print(f"{x} {sign} {y} = {result}")
    elif sign == "-":
        result = x - y
        print(f"{x} {sign} {y} = {result}")

    print("-------------------------------------")
