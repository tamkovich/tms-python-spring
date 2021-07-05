class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return f'Результат сложения: {self.a + self.b}'

    def sub(self):
        return f'Результат вычитания: {self.a - self.b}'

    def mul(self):
        return f'Резултат умножения: {self.a * self.b}'

    def div(self):
        try:
            answer = round(self.a / self.b, 10)
            return f'Результат деления: {answer}'
        except ZeroDivisionError:
            return 'ZeroDivisionError: division by zero'
