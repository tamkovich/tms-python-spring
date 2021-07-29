# Реализовать пользовательский интерфейс с бесконечным циклом.
# Добавить валидацию входных данных.

import exceptions
import func


def start_calculations() -> None:
    """Ф-ция запускает и останавливает вычисления"""
    dict_operation = {
        "+": func.add_num,
        "-": func.sub_num,
        "*": func.mul_num,
        "/": func.div_num,
    }
    while True:
        operation = input("Введите знак операции (+,-,*,/) или fin: ")
        if operation == "fin":
            print("Расчеты завершены!")
            break
        num1 = input("Введите первое число: ")
        num2 = input("Введите второе число: ")
        try:
            num1 = float(num1)
            num2 = float(num2)
            dict_operation[operation](num1, num2)
        except ValueError as v:
            print("Вы ввели не число, расчет невозможен!")
            exceptions.add_error_v(v)
            continue
        except KeyError as k:
            print("Знак операции введен не корректно!")
            exceptions.add_error_k(k)
            continue
        except ZeroDivisionError as z:
            print("На ноль делить нельзя!")
            exceptions.add_error_z(z)
            continue
