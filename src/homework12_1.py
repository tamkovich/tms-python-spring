""" Создать класс MyTime. Атрибуты: hours, minutes, seconds. Методы:
переопределить магические методы сравнения(==, !=, >=, <=, <, >),
сложения, вычитания, умножения на число, вывод на экран. Перегрузить
конструктор на обработку входных параметров вида: одна строка, три
числа, другой объект класса MyTime, и отсутствие входных параметров.
Реализовать нормальное отображение времени(12:65:83 - 13:06:23)
[my-oop-02] Задание доделать в рамках cw12"""


class MyTime:
    def __init__(self, *args):
        if args == ():
            print("No any parameters")
        elif all(isinstance(arg, int) for arg in args) and len(args) == 3:
            self.hours = args[0]
            self.minutes = args[1]
            self.seconds = args[2]
        elif type(args[0]) is str:
            arr = args[0].split(' ')
            self.hours = int(arr[0])
            self.minutes = int(arr[1])
            self.seconds = int(arr[2])
        elif type(args[0]) is MyTime:
            self.hours = args[0].hours
            self.minutes = args[0].minutes
            self.seconds = args[0].seconds
        else:
            print('Wrong data format')
            print('Try some like: 10, 10, 10; 10 10 10; instance MyTime')

    @property
    def time_in_seconds(self):
        return self.seconds + self.minutes * 60 + self.hours * 3600

    @property
    def time(self):
        # time was str -> int
        self.hours = int(self.hours)
        self.minutes = int(self.minutes)
        self.seconds = int(self.seconds)
        # (12:65:83 - 13:06:23)
        if self.seconds >= 60:
            self.hours = (self.hours % 24) + round(self.minutes / 60)
            self.minutes = (self.minutes % 60) + round(self.seconds / 60)
            self.seconds = self.seconds % 60
        elif self.minutes >= 60:
            self.hours = (self.hours % 24) + round(self.minutes / 60)
            self.minutes = (self.minutes % 60) + round(self.seconds / 60)
        elif self.hours >= 24:
            self.hours = self.hours % 24
        # view if seconds, minutes, hours < 10
        if self.seconds < 10:
            return f'Time is: {self.hours}:{self.minutes}:0{self.seconds}'
        elif self.minutes < 10:
            return f'Time is: {self.hours}:0{self.minutes}:{self.seconds}'
        if self.hours < 10:
            return f'Time is: 0{self.hours}:{self.minutes}:{self.seconds}'

    def __eq__(self, other_time: 'MyTime') -> bool:
        return self.time_in_seconds == other_time.time_in_seconds

    def __ne__(self, other_time: 'MyTime') -> bool:
        return self.time_in_seconds > other_time.time_in_seconds

    def __lt__(self, other_time: 'MyTime') -> bool:
        return self.time_in_seconds < other_time.time_in_seconds

    def __gt__(self, other_time: 'MyTime') -> bool:
        return self.time_in_seconds > other_time.time_in_seconds

    def __ge__(self, other_time: 'MyTime') -> bool:
        return self.time_in_seconds >= other_time.time_in_seconds

    def __le__(self, other_time: 'MyTime') -> bool:
        return self.time_in_seconds <= other_time.time_in_seconds

    def __add__(self, number: int):
        return self.time_in_seconds + number

    def __sub__(self, number: int):
        return self.time_in_seconds - number

    def __mul__(self, number: int):
        return self.time_in_seconds * number

    
g = MyTime()
a = MyTime(12, 65, 83)
print(a.time)
b = MyTime(a)
print(b.time_in_seconds)
c = MyTime('235 2 963')
print(c.time)
print(c.__ge__(b))
