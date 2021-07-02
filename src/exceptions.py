class InputException(Exception):
    def __init__(self, message='Wrong input!'):
        super().__init__(message)


class DivByZero(Exception):
    def __init__(self, message='Cannot divide by zero!'):
        super().__init__(message)


class NoInput(Exception):
    def __init__(self, message='Enter numbers first!'):
        super().__init__(message)
