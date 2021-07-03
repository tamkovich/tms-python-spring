import exceptions


def fun_summation(num1, num2):
    if exceptions.fun_TypeError(num1, num2, flag=0) != 1:
        return int(num1) + int(num2)


def fun_subtraction(num1, num2):
    if exceptions.fun_TypeError(num1, num2, flag=0) != 1:
        return int(num1) - int(num2)


def fun_multiplication(num1, num2):
    if exceptions.fun_TypeError(num1, num2, flag=0) != 1:
        return int(num1) * int(num2)


def fun_division(num1, num2):
    if exceptions.fun_TypeError(num1, num2, flag=0) != 1 and \
            exceptions.fun_ZeroDivisionError(num1, num2, flag=0) != 1:
        return round((int(num1) / int(num2)), 3)
