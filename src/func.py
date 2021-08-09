import exceptions


class Math:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def FunSummation(self):
        if exceptions.FunTypeError(self.num1, self.num2, flag=0) != 1:
            return int(self.num1) + int(self.num2)

    def FunSubtraction(self):
        if exceptions.FunTypeError(self.num1, self.num2, flag=0) != 1:
            return int(self.num1) - int(self.num2)

    def FunMultiplication(self):
        if exceptions.FunTypeError(self.num1, self.num2, flag=0) != 1:
            return int(self.num1) * int(self.num2)

    def FunDivision(self):
        if exceptions.FunTypeError(self.num1, self.num2, flag=0) != 1 and \
                exceptions.FunZeroDivisionError(self.num1, self.num2, flag=0) != 1:
            return round(int(self.num1) / int(self.num2), 3)
