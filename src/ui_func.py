import func


def calculate(operation, num1, num2):
    list_of_operation = {'+': func.Math(num1, num2).FunSummation(),
                         '-': func.Math(num1, num2).FunSubtraction(),
                         '*': func.Math(num1, num2).FunMultiplication(),
                         '/': func.Math(num1, num2).FunDivision()
                         }
    print(list_of_operation[operation])
