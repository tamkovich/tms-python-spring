from exceptions import DivByZero
from exceptions import InputException
from exceptions import NoInput


def add_operation_func(num1, num2):
    try:
        if num1.isalpha() or num2.isalpha():
            raise InputException
        elif not num1 or not num2:
            raise NoInput
        else:
            return int(num1) + int(num2)
    except InputException as i_e:
        return i_e
    except NoInput as n_i:
        return n_i


def minus_operation_func(num1, num2):
    try:
        if num1.isalpha() or num2.isalpha():
            raise InputException
        elif not num1 or not num2:
            raise NoInput
        else:
            return int(num1) - int(num2)
    except InputException as i_e:
        return i_e
    except NoInput as n_i:
        return n_i


def mult_operation_func(num1, num2):
    try:
        if num1.isalpha() or num2.isalpha():
            raise InputException
        elif not num1 or not num2:
            raise NoInput
        else:
            return int(num1) * int(num2)
    except InputException as i_e:
        return i_e
    except NoInput as n_i:
        return n_i


def div_operation_func(num1, num2):
    try:
        if num2 == "0":
            raise DivByZero
        elif num1.isalpha() or num2.isalpha():
            raise InputException
        elif not num1 or not num2:
            raise NoInput
        else:
            return int(num1) / int(num2)
    except DivByZero as d_b_z:
        return d_b_z
    except InputException as i_e:
        return i_e
    except NoInput as n_i:
        return n_i
