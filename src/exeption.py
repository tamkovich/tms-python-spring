"""исключение в случаи деления на ноль"""


class Zerodelite(Exception):
    def __init__(self, message="Вы разделили на ноль"):
        super().__init__(message)


if __name__ == "__main__":
    raise Zerodelite
