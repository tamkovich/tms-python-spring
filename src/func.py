from exeption import Zerodelite

"""Класс преобразующий строку в матиматическое значение """


class math_callc:
    def __init__(self, input_str: str) -> int:
        self.input_str = input_str

    """Метод преобраззующий из атрибута математическую строку"""

    def value(self):
        self.new_str = ""
        self.new_list = []
        for i in self.input_str:
            if i != "*" and i != "/" and i != "+" and i != "-":
                self.new_str += i
            else:
                self.new_list.append(self.new_str)
                self.new_str = ""
                self.new_list.append(i)
        self.new_list.append(self.new_str)
        return self.new_list

    @property
    def arg(self):
        return eval_(self.value())


"""
    Данные вложеные функции выполняют логику работы
    матиматического выражения изначалльно идет умножения
    делления потом сложения вычитания
    математическое выражение читается слево на право
"""


def eval_2(func):
    def wraper_func(list_value_2):
        new_list_arg = func(list_value_2)
        for index, value in enumerate(new_list_arg):
            if value in "+-":
                if value == "+":
                    new_list_arg[index] = str(
                        float(new_list_arg[index - 1]) + float(new_list_arg[index + 1])
                    )
                    new_list_arg[index + 1], new_list_arg[index - 1] = str(
                        new_list_arg[index]
                    ), str(new_list_arg[index])
                elif value == "-":
                    new_list_arg[index] = str(
                        float(new_list_arg[index - 1]) - float(new_list_arg[index + 1])
                    )
                    new_list_arg[index + 1], new_list_arg[index - 1] = str(
                        new_list_arg[index]
                    ), str(new_list_arg[index])
        return new_list_arg[-1]

    return wraper_func


@eval_2
def eval_(list_value):

    for index, value in enumerate(list_value):
        if value in "*/":
            if value == "*":
                list_value[index] = str(
                    float(list_value[index - 1]) * float(list_value[index + 1])
                )
                list_value[index + 1], list_value[index - 1] = str(
                    list_value[index]
                ), str(list_value[index])

            elif value == "/":

                if "0" == list_value[index + 1]:
                    raise Zerodelite
                list_value[index] = str(
                    float(list_value[index - 1]) / float(list_value[index + 1])
                )
                list_value[index + 1], list_value[index - 1] = str(
                    list_value[index]
                ), str(list_value[index])

    new_list = [
        value
        for index, value in enumerate(list_value)
        if index != (len(list_value) - 1) and value != list_value[index + 1]
    ]
    new_list.append(list_value[-1])

    return new_list


if __name__ == "__main__":
    a = math_callc("1-2*1.5/0.0")
    print(a.arg)
