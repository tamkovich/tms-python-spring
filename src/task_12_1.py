"""
Homework - 12
task_12_1: Создать класс MyTime. Атрибуты: hours, minutes, seconds.
Методы: переопределить магические методы сравнения(==, !=, >=, <=, <, >),
сложения, вычитания, умножения на число, вывод на экран. Перегрузить
конструктор на обработку входных параметров вида: одна строка, три
числа, другой объект класса MyTime, и отсутствие входных параметров.
Реализовать нормальное отображение времени( 12:65:83 - 13:06:23)
[my-oop-02] Задание доделать в рамках cw12
"""


class MyTime:
    """Класс с атрибутами + условия и переопределенными магическими методами"""
    def __init__(self, *args) -> None:
        if len(args) == 3:
            print("На входе 3 значения")
            self.hours = args[0]
            self.minutes = args[1]
            self.seconds = args[2]
        elif type(args[0]) is str:
            print(f"На входе 1 значение в виде строки: {args[0]}")
            str_time = args[0].split('-')
            self.hours = int(str_time[0])
            self.minutes = int(str_time[1])
            self.seconds = int(str_time[2])
        elif type(args[0]) is MyTime:
            print("На входе 1 значение в виде MyTime")
            copy_time = args[0]
            self.hours = copy_time.hours
            self.minutes = copy_time.minutes
            self.seconds = copy_time.seconds

    @property
    def time_in_seconds(self) -> int:
        return self.seconds + self.minutes * 60 + self.hours * 3600

    def __lt__(self, other_time: "MyTime") -> bool:
        """Ф-ция проверяет истинность x < y"""
        return self.time_in_seconds < other_time.time_in_seconds

    def __gt__(self, other_time: "MyTime") -> bool:
        """Ф-ция проверяет истинность x > y"""
        return self.time_in_seconds > other_time.time_in_seconds

    def __le__(self, other_time: "MyTime") -> bool:
        """Ф-ция проверяет истинность x ≤ y"""
        return self.time_in_seconds <= other_time.time_in_seconds

    def __ge__(self, other_time: "MyTime") -> bool:
        """Ф-ция проверяет истинность x ≥ y"""
        return self.time_in_seconds >= other_time.time_in_seconds

    def __eq__(self, other_time: "MyTime") -> bool:
        """Ф-ция проверяет истинность x == y"""
        print("Ну что, правду говорят?")
        return self.time_in_seconds == other_time.time_in_seconds

    def __ne__(self, other_time: "MyTime") -> bool:
        """Ф-ция проверяет истинность x != y"""
        print("Трындят, походу?")
        return self.time_in_seconds != other_time.time_in_seconds

    def __add__(self, other_time: "MyTime") -> int:
        """Ф-ция складывает время x + время y"""
        rez = self.time_in_seconds + other_time.time_in_seconds
        print(f"{self.hours}:{self.minutes}:{self.seconds} + "
              f"{other_time.hours}:{other_time.minutes}:{other_time.seconds} = "
              f"{rez} seconds")
        return rez

    def __sub__(self, other_time: "MyTime") -> int:
        """Ф-ция вычитает время x - y"""
        rez = self.time_in_seconds - other_time.time_in_seconds
        print(f"{self.hours}:{self.minutes}:{self.seconds} - "
              f"{other_time.hours}:{other_time.minutes}:{other_time.seconds} = "
              f"{rez} seconds")
        return rez

    def __mul__(self, num: int) -> int:
        """Ф-ция умножает время x на число num"""
        rez = self.time_in_seconds * num
        print(f"{self.hours}:{self.minutes}:{self.seconds} * {num} = "
              f"{rez} seconds")
        return rez

    def __repr__(self) -> str:
        """Ф-ция выводит на экран время x"""
        return f"{self.hours}:{self.minutes}:{self.seconds}"


if __name__ == "__main__":
    time1 = MyTime(10, 10, 10)
    time2 = MyTime(10, 30, 30)
    tmp = MyTime("10-10-30")
    print(tmp.hours)
    time3 = MyTime(time2)
    print(time3.hours)
    print(time1 < time2)
    print(time1 == time1)
    print(time1 != time2)
    time5 = MyTime(1, 0, 0)
    time6 = MyTime(2, 2, 3)
    print(time6 + time5)
    print(time6 - time5)
    print(time5 * 3)
    print(time6)

# Денис, задание сделал, но осталось пару не совсем понятных моментов
# (если не затруднит прокомментируй их коротко плиз при review):
# 1. Не совсем понял зачем здесь @property (чисто чтобы отбросить () или смысл в другом) ?
# 2. Я думал @property и  @ .setter используют ТОЛЬКО с приватными атриб. для облегчения доступа?
# 3. Почему в def __...__ мы передаем только other_time и сравниваем его с self, а не 2 объекта MyTime
#    передаем и сравниваем (так у меня не получилось)? (при решении сохранил твой авторский шаблон)
