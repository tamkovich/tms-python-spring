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
    """Class of time instance

    Represents a time in a moment of day.
    Days are not counted: if time exceeds 24 hours MyTime instance will contain
    only time after 00:00:00.
    For example: time 30:15:12 represents as 06:15:12.
    The seconds exceeds 60 are carried over the minutes.
    The minutes exceeds 60 are carried over the hours.

    There is four read-only attributes available in the instance of MyTime:
        hours - represents hours,
        minutes - represents minutes,
        seconds - represents seconds,
        absolute_time - represents time in seconds from the beginning of the day

    The next operations is available for MyTime instances:
        <, >, <=, >=, ==, != - comparisons;
        +, - - addition and subtraction with related objects;
        * - multiplication by a number.

    When using the instance directly in string operations,
    the instance is represented as a string, for example, "19:15:20"
    """

    def __init__(self, hours: int = 0, minutes: int = 0, seconds: int = 0,
                 time_str: str = None, time_obj: 'MyTime' = None):
        """Constructor of MyTime instance

        :param hours: int value represents hours
        :param minutes: int value represents minutes
        :param seconds: int value represents seconds
        :param time_str: string value represents time.
                String have to contain hours, minutes, seconds
                split with symbols ":", ".", "-"
        :param time_obj: instance of MyTime

        Correct call examples:

        MyTime() - create instance "00:00:00"
        MyTime(19,7,7) - create instance "19:07:07"
        MyTime(19) - create instance "19:00:00"
        MyTime(minutes=19) - create instance "00:19:00"
        MyTime(seconds=19) - create instance "00:00:19",
            and so on when using combinations of named parameters hours, minutes, seconds
        MyTime(time_str = "11:07:15"),
        MyTime(time_str = "11.07.15"),
        MyTime(time_str = "11-07-15") - create instance "11:07:15"

        time_1 = MyTime(time_str="16.25.10")
        MyTime(time_obj=time_1) - create copy of instance time_1

        The constructor should only be called with the variants of the argument sets
        shown in the examples above. Otherwise, an exception is raised.
        """

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
        if any(arg < 0 for arg in [hours, minutes, seconds]):
            raise ValueError("Negative values of hours, minutes or seconds is restricted.")

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

    def __create_from_obj(self, time_obj: 'MyTime'):
        self.__hours = time_obj.hours
        self.__minutes = time_obj.minutes
        self.__seconds = time_obj.seconds
        self.__update_absolute_time()

    def __update_absolute_time(self):
        self.__absolute_time = self.seconds + self.minutes * 60 + self.hours * 3_600

    @staticmethod
    def __expand_abs_time(abs_time: int) -> 'tuple(int, int, int)':
        if abs_time < 0:
            abs_time += 86_400

        hours = abs_time // 3600
        minutes = abs_time % 3600 // 60
        seconds = abs_time % 3600 % 60
        return hours, minutes, seconds

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

    def __add__(self, other: 'MyTime'):
        if isinstance(other, MyTime):
            return MyTime(self.hours + other.hours,
                          self.minutes + other.minutes,
                          self.seconds + other.seconds)
        else:
            return self

    def __sub__(self, other: 'MyTime'):
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
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"


def run():
    t0 = MyTime()
    t1 = MyTime(25, 4, 250)
    t2 = MyTime(time_obj=t1 - t1 * 2)
    t3 = MyTime(time_str="17:61:66")

    print(f"t0 = {t0}\nt1 = {t1}\nt2 = {t2}\nt3 = {t3}\n")

    print(f"t0 == t0 {t0 == t0}")
    print(f"t1 == t2 {t1 == t2}")
    print(f"t1 != t2 {t1 != t2}")
    print(f"t1 > t2 {t1 > t2}")
    print(f"t1 < t2 {t1 < t2}")
    print(f"t1 >= t2 {t1 >= t2}")
    print(f"t1 <= t2 {t1 <= t2}\n")

    try:  # 1
        t0 = MyTime(-11)
    except (TypeError, ValueError) as error:
        print(f"Try 1: {error}")

    try:  # 2
        t0 = MyTime(time_str="12/12/04")
    except (TypeError, ValueError) as error:
        print(f"Try 2: {error}")

    try:  # 3
        t0 = MyTime(time_str=12)
    except (TypeError, ValueError) as error:
        print(f"Try 3: {error}")

    try:  # 4
        t0 = MyTime(time_obj=12)
    except (TypeError, ValueError) as error:
        print(f"Try 4: {error}")

    try:  # 5
        t0 = MyTime("12")
    except (TypeError, ValueError) as error:
        print(f"Try 5: {error}")


if __name__ == "__main__":
    run()
