import func

def calculation(operation, num1, num2):
    if operation == '+':
        print(func.fun_summation(num1, num2))
    if operation == '-':
        print(func.fun_subtraction(num1, num2))
    if operation == '*':
        print(func.fun_multiplication(num1, num2))
    if operation == '/':
        print(func.fun_division(num1, num2))
