from exceptions import DivByZero
from exceptions import InputException


def add_operation_func(num1, num2):
    try:
        if num1.isalpha() or num2.isalpha():
            raise InputException
        else:
            return int(num1) + int(num2)
    except InputException as i_e:
        return i_e


def minus_operation_func(num1, num2):
    try:
        if num1.isalpha() or num2.isalpha():
            raise InputException
        else:
            return int(num1) - int(num2)
    except InputException as i_e:
        return i_e


def mult_operation_func(num1, num2):
    try:
        if num1.isalpha() or num2.isalpha():
            raise InputException
        else:
            return int(num1) * int(num2)
    except InputException as i_e:
        return i_e


def div_operation_func(num1, num2):
    try:
        if num2 == "0":
            raise DivByZero
        if num1.isalpha() or num2.isalpha():
            raise InputException
        else:
            return int(num1) / int(num2)
    except DivByZero as d_b_z:
        return d_b_z
    except InputException as i_e:
        return i_e
