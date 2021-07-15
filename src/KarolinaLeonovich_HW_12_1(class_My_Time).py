"""Создать класс MyTime. Атрибуты: hours, minutes, seconds. Методы:
переопределить магические методы сравнения(==, !=, >=, <=, <, >),
сложения, вычитания, умножения на число, вывод на экран. Перегрузить
конструктор на обработку входных параметров вида: одна строка, три
числа, другой объект класса MyTime, и отсутствие входных параметров.
Реализовать нормальное отображение времени(12:65:83 - 13:06:23)
[my-oop-02] Задание доделать в рамках cw12"""


class TimeMultException(Exception):
    def __init__(self, message="time can only be multiplied by a number"):
        super().__init__(message)


class MyTime:
    def __init__(self, *args):
        if args:
            if all(isinstance(arg, int) for arg in args):
                self.hours = args[0]
                self.minutes = args[1]
                self.seconds = args[2]
            elif all(isinstance(arg, MyTime) for arg in args):
                self.hours = args[0].hours
                self.minutes = args[0].minutes
                self.seconds = args[0].seconds
            elif all(isinstance(arg, str) for arg in args):
                self.hours = int(args[0].split()[0])
                self.minutes = int(args[0].split()[1])
                self.seconds = int(args[0].split()[2])
            self.minutes = self.minutes + self.seconds // 60
            self.seconds = self.seconds % 60
            self.hours = (self.hours + self.minutes // 60) % 24
            self.minutes = self.minutes % 60
            self.clean_seconds = self.seconds + self.minutes * 60 + self.hours * 60 * 60
        else:
            self.hours = 0
            self.minutes = 0
            self.seconds = 0

    def __str__(self):
        return f"{self.hours}:{self.minutes}:{self.seconds}"

    def __eq__(self, other):
        return self.clean_seconds == other.clean_seconds

    def __ne__(self, other):
        return self.clean_seconds != other.clean_seconds

    def __lt__(self, other):
        return self.clean_seconds < other.clean_seconds

    def __gt__(self, other):
        return self.clean_seconds > other.clean_seconds

    def __le__(self, other):
        return self.clean_seconds <= other.clean_seconds

    def __ge__(self, other):
        return self.clean_seconds >= other.clean_seconds

    def __len__(self):
        return 1001

    def __add__(self, other):
        sum_amount = self.clean_seconds + other.clean_seconds
        return f"{sum_amount // 3600 % 24}:{sum_amount //60 % 60}:{sum_amount % 60}"

    def __sub__(self, other):
        sub_amount = abs(self.clean_seconds - other.clean_seconds)
        return f"{sub_amount // 3600 % 24}:{sub_amount //60 % 60}:{sub_amount % 60}"

    def __mul__(self, other):
        if type(other) != int and type(other) != float:
            raise TimeMultException
        else:
            mul_amount = self.clean_seconds * other
            return (
                f"{mul_amount // 3600 % 24}:{mul_amount // 60 % 60}:{mul_amount % 60}"
            )
