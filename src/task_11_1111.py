"""
Homework - 11
task_11_11.11:
Добавить два новых атрибута в родительский класс: weight и height.
Добавить методы change_weight, change_height принимающий один параметр
и прибавляющий его к соответствующему аргументу. Если параметр не был
передан, увеличивать на 0.2.
Изменить метод fly класса Parrot. Если вес больше 0.1 выводить сообщение
This parrot cannot fly.
"""


# def func(n: int) -> int:


class Bird:
    """ Создан родительский класс"""

    def __init__(self, color: str) -> None:
        self.color = color

    def fly(self) -> None:
        print("Лечууу!")


class Parrot(Bird):
    """ Создан дочерний класс с доп. атрибутами и методами"""

    def __init__(self, color: str, weight: float, height: int) -> None:
        self.color = color
        self.weight = weight
        self.height = height

    def change_weight(self, weight=0.2) -> None:
        self.weight += weight

    def change_height(self, height=0.2) -> None:
        self.height += height

    def fly(self) -> None:
        if self.weight > 0.1:
            print("This parrot cannot fly")
        else:
            print("Лечууу!")


if __name__ == "__main__":
    popka = Parrot("black", 0.09, 11)
    print(popka.color)
    popka.fly()
    print(popka.height)
    popka.change_height(9)
    print(popka.height)
    kesha = Parrot("pink", 0.08, 12)
    print(kesha.color)
    kesha.fly()
    print(kesha.weight)
    kesha.change_weight()
    kesha.fly()
    print(kesha.weight)
