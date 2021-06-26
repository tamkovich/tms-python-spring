from exceptions import OperationTypeException
from classes import Math


def get_user_choice() -> str:
    CHOICE_SET = {"+", "-", "/", "*", "0"}

    choice = input("\nOperation type (+, –, /, *) or 0 for exit: ")
    if choice not in CHOICE_SET:
        raise OperationTypeException
    else:
        return choice


def get_operands() -> 'tuple(float, float)':
    x = float(input("The first number: "))
    y = float(input("The second number: "))
    return x, y


def calculate(operation: str, math: 'Math') -> float:
    OPERATIONS = {"+": math.add,
                  "-": math.subtract,
                  "*": math.multiply,
                  "/": math.divide
                  }

    return OPERATIONS[operation]()
