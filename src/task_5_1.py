"""
Написать программу, в которой вводятся два операнда Х и Y и знак операции
sign (+, –, /, *). Вычислить результат Z в зависимости от знака. Предусмотреть
реакции на возможный неверный знак операции, а также на ввод Y=0 при
делении. Организовать возможность многократных вычислений без перезагрузки
программа (т.е. построить бесконечный цикл). В качестве символа прекращения
вычислений принять ‘0’ (т.е. sign='0') is None:
"""
while True:
    x = float(input("Введите число:"))
    sign = input("Введите знак операции:")
    y = float(input("Введите число:"))
    if sign == "+":
        z = x + y
        print(z)
    elif sign == "-":
        z = x - y
        print(z)
    elif sign == "*":
        z = x * y
        print(z)
    elif sign == "/":
        if y != 0:
            z = x / y
            print(z)
        else:
            print('На ноль делить нельзя!')
    elif sign != "+" or "-" or "*" or "/" or "0":
        print('Неверный знак!')
    if sign == "0":
        break
