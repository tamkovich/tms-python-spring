"""
     Создае свое исключение для вызова
     экземпляра класса без параметров
"""


class MyTimeExeption(Exception):
    def __init__(self, messege="ars is object NONE") -> None:
        super().__init__(messege)


class MyTime:
    def __init__(self, *args):
        if args:
            if len(args) == 3:
                print("На входе 3 значения")
                self.hours = args[0]
                self.minutes = args[1]
                self.seconds = args[2]
            elif type(args[0]) is str:
                print(f"На входе 1 значение в виде строки: {args[0]}")
                arr = args[0].split("-")
                self.hours = int(arr[0])
                self.minutes = int(arr[1])
                self.seconds = int(arr[2])
            elif type(args[0]) is MyTime:
                print("На входе 1 значение в виде MyTime")
                copy_time = args[0]
                self.hours = copy_time.hours
                self.minutes = copy_time.minutes
                self.seconds = copy_time.seconds
        else:
            """
            Значение args Folse значит был
            вызван класс без параметров
            вызываем свое исключение
            """
            try:
                raise MyTimeExeption
            except MyTimeExeption:
                print("Вы вызвали класс без параметров")

    @property
    def time_in_seconds(self):
        return self.seconds + self.minutes * 60 + self.hours * 3600

    def __lt__(self, other_time: "MyTime") -> bool:
        return self.time_in_seconds < other_time.time_in_seconds

    def __gt__(self, other_time: "MyTime") -> bool:
        return self.time_in_seconds > other_time.time_in_seconds

    def __eq__(self, other_time: "MyTime") -> bool:
        return self.time_in_seconds == other_time.time_in_seconds

    def __ne__(self, other_time: "MyTime") -> bool:
        return self.time_in_seconds != other_time.time_in_seconds

    def __le__(self, other_time: "MyTime") -> bool:
        return self.time_in_seconds <= other_time.time_in_seconds

    def __ge__(self, other_time: "MyTime") -> bool:
        return self.time_in_seconds >= other_time.time_in_seconds


time1 = MyTime(11, 11, 11)
time2 = MyTime("11-11-12")
time3 = MyTime(time1)
"""проверяем магические методы"""
print(f"равенство time3 == time1:{time3 == time1}")
print(f"равенство time2 == time1:{time2 == time1}")
print(f"больше time2 > time1:{time2 > time1}")
