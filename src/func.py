import exceptions


class Math:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def fun_summation(self):
        if exceptions.fun_TypeError(self.num1, self.num2, flag=0) != 1:
            return int(self.num1) + int(self.num2)

    def fun_subtraction(self):
        if exceptions.fun_TypeError(self.num1, self.num2, flag=0) != 1:
            return int(self.num1) - int(self.num2)

    def fun_multiplication(self):
        if exceptions.fun_TypeError(self.num1, self.num2, flag=0) != 1:
            return int(self.num1) * int(self.num2)

    def fun_division(self):
        if exceptions.fun_TypeError(self.num1, self.num2, flag=0) != 1 and \
                exceptions.fun_ZeroDivisionError(self.num1, self.num2, flag=0) != 1:
            return round(int(self.num1) / int(self.num2), 3)
