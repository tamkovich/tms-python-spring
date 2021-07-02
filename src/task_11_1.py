"""
Создать класс MyTime. Атрибуты: hours, minutes, seconds. Методы:
переопределить магические методы сравнения(==, !=, >=, <=, <, >),
сложения, вычитания, умножения на число, вывод на экран. Перегрузить
конструктор на обработку входных параметров вида: одна строка, три
числа, другой объект класса MyTime, и отсутствие входных параметров.
Реализовать нормальное отображение времени(12:65:83 - 13:06:23)
"""
from datetime import datetime
from datetime  import timedelta


class MyTime:
    def __init__(self, *args):
        if all(isinstance(arg, int) for arg in args):
            self.hours = args[0]
            self.minutes = args[1]
            self.seconds = args[2]
        if all(isinstance(arg, str) for arg in args):
            self.hours = int(args[0].split()[0])
            self.minutes = int(args[0].split()[1])
            self.seconds = int(args[0].split()[2])
        if all(isinstance(arg, MyTime) for arg in args):
            self.hours = args[0].hours
            self.minutes = args[0].minutes
            self.seconds = args[0].seconds
        self.time1 = timedelta(hours=self.hours, minutes=self.minutes, seconds=self.seconds)

    # магический метод " == "
    def __eq__(self, other):
        return self.time1 == other.time1

    # магический метод " != "
    def __ne__(self, other):
        return self.time1 != other.time1

    # магический метод " > "
    def __gt__(self, other):
        return self.time1 > other.time1

    # магический метод " >= "
    def __ge__(self, other):
        return self.time1 >= other.time1

    # магический метод " < "
    def __lt__(self, other):
        return self.time1 < other.time1

    # магический метод " <= "
    def __le__(self, other):
        return self.time1 <= other.time1

    # магический метод " + "
    def __add__(self, other):
        return self.time1 + other.time1

    # магический метод " - "
    def __sub__(self, other):
        return self.time1 - other.time1

    # магический метод " * "
    def __mul__(self, other):
        return self.time1 * other.time1

    # магический метод вывода на экран
    def __repr__(self):
        return f"{self.time1}"


time_ = MyTime("12 65 83")

time2 = datetime.now()
time_today = time2.strftime("%X")

created_time = time_.hours * 3600 + time_.minutes * 60 + time_.seconds
time_now = time2.hour + time2.minute + time2.second

print(f"{time_.time1}")
print(f"time1 == time2 {created_time == time_now}")
print(f"time1 != time2 {created_time != time_now}")
print(f"time1 > time2 {created_time > time_now}")
print(f"time1 >= time2 {created_time >= time_now}")
print(f"time1 < time2 {created_time < time_now}")
print(f"time1 <= time2 {created_time <= time_now}")
print(f"time1 + time2 {time_.time1 + time2}")
print(f"time1 - time2 {created_time - time_now}")
print(f"time1 * time2 {created_time * time_now}")
