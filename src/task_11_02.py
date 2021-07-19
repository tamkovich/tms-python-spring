"""Задание 11.2.

Создать класс Car. Атрибуты: марка, модель, год выпуска, скорость(по
умолчанию 0). Методы: увеличить скорости(скорость + 5), уменьшение
скорости(скорость - 5), стоп(сброс скорости на 0), отображение скорости,
разворот(изменение знака скорости). Все атрибуты приватные."""

from task_11_01 import Vehicle


class Car(Vehicle):
    def __init__(self, firm: str, model: str, year: int, speed=0):
        super().__init__(firm, model, year)
        self.speed = speed

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed):
        self.__speed = speed

    def speed_increase(self, delta=5):
        self.speed += delta

    def speed_decrease(self, delta=5):
        self.speed -= delta

    def stop_car(self):
        self.speed = 0

    def speed_reverse(self):
        self.speed *= -1

    def show_speed(self):
        print(f"Current speed is {self.speed}")


if __name__ == "__main__":
    car = Car("BMW", "X6", 2020, 120)

    print(car.get_info())
    car.show_speed()

    car.speed_decrease()
    car.show_speed()

    car.speed_decrease(15)
    car.show_speed()

    car.speed_increase()
    car.show_speed()

    car.speed_increase(2)
    car.show_speed()

    car.speed_reverse()
    car.show_speed()

    car.stop_car()
    car.show_speed()
