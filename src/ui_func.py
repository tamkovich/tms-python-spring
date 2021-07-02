from exceptions import DivByZero
from exceptions import InputException
from exceptions import NoInput


def ui_func():
    operations = ("/", "*", "+", "-")
    try:
        num1 = input("Enter the first number ...")
        num2 = input("Enter the second number...")
        operator = input("Enter /, *, +, or - ")
        if not all([num1, num2, operator]):
            raise NoInput
        elif not all(
                [num1.isdigit(), num2.isdigit(), operator in operations]
        ):
            raise InputException
        elif num2 == "0" and operator == "/":
            raise DivByZero
        return int(num1), int(num2), operator
    except InputException as i_e:
        print(i_e)
    except DivByZero as d_b_z:
        print(d_b_z)
    except NoInput as n_i:
        print(n_i)
