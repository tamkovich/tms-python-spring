import func


def fun_calculation(operation, num1, num2):
    list_of_operation = {'+' : func.Math(num1, num2).fun_summation(),
                         '-' : func.Math(num1, num2).fun_subtraction(),
                         '*' : func.Math(num1, num2).fun_multiplication(),
                         '/' : func.Math(num1, num2).fun_division()
                         }
    print(list_of_operation[operation])
