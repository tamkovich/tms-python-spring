# 1) Написать программу, в которой вводятся два операнда Х и Y и знак операции
# sign (+, –, /, *). Вычислить результат Z в зависимости от знака. Предусмотреть
# реакции на возможный неверный знак операции, а также на ввод Y=0 при
# делении. Организовать возможность многократных вычислений без перезагрузки
# программа (т.е. построить бесконечный цикл). В качестве символа прекращения
# вычислений принять ‘0’ (т.е. sign='0').
x = 0
y = 0
sign = '*'
result_z = 0
while True:
    x = int(input("введите число 1"))
    sign = input("введите знак операции (+, –, /, *)")
    y = int(input("введите число 2"))
    if y == 0 and sign == '/':
        print("на ноль делить нельзя")
        continue
    if sign == '+':
        result_z = x + y
        print(result_z)
        continue
    elif sign == '-':
        result_z = x - y
        print(result_z)
        continue
    elif sign == '/':
        result_z = x / y
        print(result_z)
        continue
    elif sign == '*':
        result_z = x * y
        print(result_z)
        continue
    elif int(sign) == 0:
        print("выход")
        break
