# Написать калькулятор. Программа должна содержать 4 функции
# принимающие два аргумента и возвращающие результаты сложения,
# вычитания, умножения и деления. Реализовать пользовательский
# интерфейс с бесконечным циклом. Добавить валидацию входных данных.
# Программа должна состоять из четырех файлов(main.py, func.py, ui_func.py
# exceptions.py). [my-oop-t05]


from func import add_operation_func
from func import div_operation_func
from func import minus_operation_func
from func import mult_operation_func


from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtGui import QFont

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QStyleFactory
from PyQt5.QtWidgets import QTextEdit

import sys

from ui_func import number_1_style
from ui_func import number_2_style


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Background, QtCore.Qt.black)
        self.setPalette(palette)
        self.setFixedSize(170, 600)
        self.setWindowTitle("Четкий калькулятор")

        self.textEdit_first_number = QTextEdit(self)
        self.textEdit_first_number.setGeometry(10, 10, 50, 50)
        self.textEdit_first_number.setStyleSheet(number_1_style)
        self.textEdit_first_number.setFont(QFont('Fixedsys'))

        self.textEdit_second_number = QTextEdit(self)
        self.textEdit_second_number.setGeometry(100, 10, 50, 50)
        self.textEdit_second_number.setStyleSheet(number_1_style)
        self.textEdit_second_number.setFont(QFont('Fixedsys'))

        self.btn_plus = QPushButton(" + ", self)
        self.btn_plus.setGeometry(40, 80, 30, 30)
        self.btn_plus.setStyleSheet(number_2_style)
        self.btn_plus.setFont(QFont('Fixedsys'))

        self.btn_minus = QPushButton(" - ", self)
        self.btn_minus.setGeometry(90, 80, 30, 30)
        self.btn_minus.setStyleSheet(number_2_style)
        self.btn_minus.setFont(QFont('Fixedsys'))

        self.btn_mult = QPushButton(" * ", self)
        self.btn_mult.setGeometry(40, 120, 30, 30)
        self.btn_mult.setStyleSheet(number_2_style)
        self.btn_mult.setFont(QFont('Fixedsys'))

        self.btn_div = QPushButton(" / ", self)
        self.btn_div.setGeometry(90, 120, 30, 30)
        self.btn_div.setStyleSheet(number_2_style)
        self.btn_div.setFont(QFont('Fixedsys'))

        self.label_warning = QTextEdit(self)
        self.label_warning.setGeometry(10, 170, 150, 420)
        self.label_warning.setStyleSheet(number_1_style)
        self.label_warning.setFont(QFont('Fixedsys'))

        self.btn_plus.clicked.connect(self.btn_plus_func)
        self.btn_minus.clicked.connect(self.btn_minus_func)
        self.btn_mult.clicked.connect(self.btn_mult_func)
        self.btn_div.clicked.connect(self.btn_div_func)

    def btn_plus_func(self):
        operator = " + "
        operand1 = self.textEdit_first_number.toPlainText()
        operand2 = self.textEdit_second_number.toPlainText()
        result = add_operation_func(operand1, operand2)
        self.label_warning.append(f"{operand1}{operator}{operand2} = {result}")

    def btn_minus_func(self):
        operator = " - "
        operand1 = self.textEdit_first_number.toPlainText()
        operand2 = self.textEdit_second_number.toPlainText()
        result = minus_operation_func(operand1, operand2)
        self.label_warning.append(f"{operand1}{operator}{operand2} = {result}")

    def btn_mult_func(self):
        operator = " * "
        operand1 = self.textEdit_first_number.toPlainText()
        operand2 = self.textEdit_second_number.toPlainText()
        result = mult_operation_func(operand1, operand2)
        self.label_warning.append(f"{operand1}{operator}{operand2} = {result}")

    def btn_div_func(self):
        operator = " / "
        operand1 = self.textEdit_first_number.toPlainText()
        operand2 = self.textEdit_second_number.toPlainText()
        result = div_operation_func(operand1, operand2)
        self.label_warning.append(f"{operand1}{operator}{operand2} = {result}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create('Fusion'))
    ex = Main()
    ex.show()
    sys.exit(app.exec_())
