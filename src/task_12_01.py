""" Задание 12.01
Создать класс MyTime.
Атрибуты: hours, minutes, seconds.
Методы: переопределить магические методы сравнения(==, !=, >=, <=, <, >),
сложения, вычитания, умножения на число, вывод на экран. Перегрузить
конструктор на обработку входных параметров вида: одна строка, три
числа, другой объект класса MyTime, и отсутствие входных параметров.
Реализовать нормальное отображение времени(​ 12:65:83​- 13:06:23)
"""


class MyTime:
    """

    """
    def __init__(self, hours=0, minutes=0, seconds=0, time_str=None, time_obj=None):
        if time_str is None and time_obj is None and all(isinstance(arg, int)
                                                         for arg in [hours, minutes, seconds]):
            self.__create_from_int(hours, minutes, seconds)
        elif all([time_str is not None, isinstance(time_str, str), time_obj is None]):
            self.__create_from_str(time_str)
        elif all([time_obj is not None, isinstance(time_obj, MyTime), time_str is None]):
            self.__create_from_obj(time_obj)
        else:
            raise TypeError("Unsupported type or set of arguments.")

    def __create_from_int(self, hours: int, minutes: int, seconds: int):
        self.__seconds = seconds % 60
        self.__minutes = (minutes + seconds // 60) % 60
        self.__hours = (hours + (minutes + seconds // 60) // 60) % 24
        self.__update_absolute_time()

    def __create_from_str(self, time_string: str):
        delimiters = [":", ".", "-"]
        for delimiter in delimiters:
            if time_string.replace(delimiter, "", 2).isdigit():
                hours, minutes, seconds = (int(item) for item in time_string.split(delimiter))
                self.__create_from_int(hours, minutes, seconds)
                break
        else:
            raise ValueError("Incompatible symbols in string.")

    def __create_from_obj(self, time_obj):
        self.__hours = time_obj.hours
        self.__minutes = time_obj.minutes
        self.__seconds = time_obj.seconds
        self.__update_absolute_time()

    @property
    def hours(self):
        return self.__hours

    @property
    def minutes(self):
        return self.__minutes

    @property
    def seconds(self):
        return self.__seconds

    @property
    def absolute_time(self):
        return self.__absolute_time

    def __expand_abs_time(self, abs_time: int):
        if abs_time < 0:
            abs_time += 86_400
        hours = abs_time // 3600
        minutes = abs_time % 3600 // 60
        seconds = abs_time % 3600 % 60
        return hours, minutes, seconds

    def __update_absolute_time(self):
        self.__absolute_time = self.seconds + self.minutes * 60 + self.hours * 3_600

    def __eq__(self, other):
        return isinstance(other, MyTime) and self.absolute_time == other.absolute_time

    def __ne__(self, other):
        return isinstance(other, MyTime) and self.absolute_time != other.absolute_time

    def __ge__(self, other):
        return isinstance(other, MyTime) and self.absolute_time >= other.absolute_time

    def __le__(self, other):
        return isinstance(other, MyTime) and self.absolute_time <= other.absolute_time

    def __gt__(self, other):
        return isinstance(other, MyTime) and self.absolute_time > other.absolute_time

    def __lt__(self, other):
        return isinstance(other, MyTime) and self.absolute_time < other.absolute_time

    def __add__(self, other):
        if isinstance(other, MyTime):
            return MyTime(self.hours + other.hours,
                          self.minutes + other.minutes,
                          self.seconds + other.seconds)
        else:
            return self

    def __sub__(self, other):
        if isinstance(other, MyTime):
            abs_time = self.absolute_time - other.absolute_time
            return MyTime(*self.__expand_abs_time(abs_time))
        else:
            return self

    def __mul__(self, other: int):
        if isinstance(other, int):
            abs_time = self.absolute_time * other
            return MyTime(*self.__expand_abs_time(abs_time))
        else:
            return self

    def __str__(self):
        return f"{self.hours}:{self.minutes}:{self.seconds}"

#-----------------------------------------------------------------------
t1 = MyTime(25, 4, 250)
t2 = MyTime(time_obj=t1 - t1*2)
t3 = MyTime(time_str="12.44.400")

print(t1, t2, t3)

print(t1 == t2)
print(t1 != t2)
print(t1 > t2)
print(t1 < t2)
print(t1 >= t2)
print(t1 <= t2)