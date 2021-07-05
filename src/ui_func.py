from exceptions import ChoiceException
import func


def start():
    answer = ''
    while answer != 'n':
        ask = input('Введите знак операции (+, -, * либо /). ')
        if ask in ('+', '-', '*', '/'):
            try:
                a = float(input('write number '))
                b = float(input('write number '))
                if ask == '+':
                    print(func.add(a, b))
                if ask == '-':
                    print(func.sub(a, b))
                if ask == '*':
                    print(func.mul(a, b))
                if ask == '/':
                    print(func.div(a, b))
            except ValueError:
                print('Вводите численные значения. ')
        else:
            raise ChoiceException
        answer = input('Вы хотите продолжить? Если нет, введите n ')
