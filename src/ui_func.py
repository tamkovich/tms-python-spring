from exceptions import ChoiceException
import classes


def start():
    answer = ''
    while answer != 'n':
        ask = input('Введите знак операции (+, -, * либо /). ')
        if ask in ('+', '-', '*', '/'):
            try:
                a = float(input('write number '))
                b = float(input('write number '))
                if ask == '+':
                    print(classes.Math(a, b).add())
                if ask == '-':
                    print(classes.Math(a, b).sub())
                if ask == '*':
                    print(classes.Math(a, b).mul())
                if ask == '/':
                    print(classes.Math(a, b).div())
            except ValueError:
                print('Вводите численные значения. ')
        else:
            raise ChoiceException
        answer = input('Вы хотите продолжить? Если нет, введите n ')
