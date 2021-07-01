
class ZeroDivisionException(Exception):
    def __init__(self, message="Деление на 0 недопустимо"):
        super().__init__(message)


class NotValidSymbolException(Exception):
    def __init__(self, message="Оператор не распознан"):
        super().__init__(message)

