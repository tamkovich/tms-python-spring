import func


def Calculation(operation, num1, num2):
    if operation == '+':
        return func.FunSummation(num1, num2)
    if operation == '-':
        return func.FunSubtraction(num1, num2)
    if operation == '*':
        return func.FunMultiplication(num1, num2)
    if operation == '/':
        return func.funDivision(num1, num2)
