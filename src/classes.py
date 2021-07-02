class Math:
    def __init__(self, x, y, operation):
        self.x = x
        self.y = y
        self.operation = operation

    def addition(self):
        return self.x + self.y

    def subtraction(self):
        return self.x - self.y

    def multiplication(self):
        return self.x - self.y

    def division(self):
        return self.x - self.y

    def __str__(self):
        if self.operation == "/":
            result = self.division()
        elif self.operation == "*":
            result = self.multiplication()
        elif self.operation == "-":
            result = self.subtraction()
        elif self.operation == "+":
            result = self.addition()
        return str(result)
