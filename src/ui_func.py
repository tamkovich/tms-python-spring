"""Создаем форму для пользовательского инерфейса"""

from tkinter import Button
from tkinter import Tk
from tkinter import Label
from func import math_callc
from exeption import Zerodelite

"""
    Создаем класс для определения
    размеров и названия формы калькулятора
"""


class FormCalc(Tk):
    def __init__(self, name: str, size_window: str):
        self.__name = name
        self.__size_window = size_window
        super().__init__()
        self.__name_form()
        self.__size_window_form()

    """метод для названия"""

    def __name_form(self):
        super().title(self.__name)

    """метод для размера формы"""

    def __size_window_form(self):
        super().geometry(self.__size_window)


"""
    Класс для создания кнопок на
    форме и отображения вводимых цифр
"""


class ButtonForm(Button):
    def __init__(self, text_btn="987+*654-/3210=DC.") -> Button:
        self.text_btn = text_btn
        super().__init__()
        self.ui_btn()

    """метод для создания кнопок и вводимых значений"""

    def ui_btn(self):
        self.formula = "0"
        """объект куда где будут отображаться вводимых с кнопок символов"""
        self.lbl = Label(
            text=self.formula,
            font=("Times New Roman", 21, "bold"),
            bg="#FFF",
            foreground="#000",
        )
        self.lbl.place(x=11, y=50)
        x = 10
        y = 130
        """создаем обьект кнопки и задаем им логику работы через лямда функцию и передаем обьекту"""
        for bt in self.text_btn:
            com = lambda x=bt: self.logicalc(x)
            Button(text=bt, bg="#FFF", font=("Times New Roman", 15), command=com).place(
                x=x, y=y, width=50, height=50
            )
            x += 50
            if x > 210:
                x = 10
                y += 50

    """Метод логики работы кнопок"""

    def logicalc(self, operation=""):
        if operation == "C":
            self.formula = ""
        elif operation == "D":
            self.formula = self.formula[0:-1]
        elif operation == "=":
            try:
                """Объект вычисляющий значения из полученой стрроки"""
                obj = math_callc(self.formula)
                self.formula = str(obj.arg)
            except Zerodelite:
                self.formula = "Нельзя делить на ноль"
        else:
            if self.formula == "0":
                self.formula = ""
            self.formula += operation
            if self.formula == ".":
                self.formula = f"0{operation}"
        self.update()

    """Метод передачи в обект Label значения для отображения"""

    def update(self):
        if self.formula == "":
            self.formula = "0"
        self.lbl.configure(text=self.formula)


"""Функция запуска приложения"""


def main():
    form = FormCalc("calc", "300x330")
    form.mainloop()


if __name__ == "__main__":
    main()
