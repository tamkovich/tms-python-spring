def FunTypeError(num1, num2, flag):
    try:
        int(num1)
        int(num2)
    except ValueError:
        flag = 1
        print("Введите число")
    return flag


def FunZeroDivisionError(num1, num2, flag):
    try:
        int(num1) / int(num2)
    except ZeroDivisionError:
        flag = 1
        print("На ноль делить нельзя!")
    return flag
