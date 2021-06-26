from exceptions import OperationTypeException
import func as fn


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


def calculate(operation: str, a: float, b: float) -> float:
    OPERATIONS = {"+": fn.add,
                  "-": fn.subtract,
                  "*": fn.multiply,
                  "/": fn.divide
                  }

    return OPERATIONS[operation](a, b)
