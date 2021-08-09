import exceptions


def FunSummation(num1, num2):
    if exceptions.FunTypeError(num1, num2, flag=0) != 1:
        return int(num1) + int(num2)


def FunSubtraction(num1, num2):
    if exceptions.FunTypeError(num1, num2, flag=0) != 1:
        return int(num1) - int(num2)


def FunMultiplication(num1, num2):
    if exceptions.FunTypeError(num1, num2, flag=0) != 1:
        return int(num1) * int(num2)


def funDivision(num1, num2):
    if exceptions.FunTypeError(num1, num2, flag=0) != 1 and \
            exceptions.FunZeroDivisionError(num1, num2, flag=0) != 1:
        return round((int(num1) / int(num2)), 3)
