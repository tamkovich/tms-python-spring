"""
Homework - 11
task_11_2: Создать класс Car. Атрибуты: марка, модель, год выпуска, скорость
(по умолчанию 0). Методы: увеличить скорости(скорость + 5), уменьшение
скорости(скорость - 5), стоп(сброс скорости на 0), отображение скорости,
разворот(изменение знака скорости). Все атрибуты приватные.
"""


class Car:
    """Класс авто с характеристиками и методами изменения скорости"""
    def __init__(self, brand: str, model: str, year: int, speed: int) -> None:
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__speed = speed

    @property
    def brand(self) -> str:
        return self.__brand

    @brand.setter
    def brand(self, brand: str) -> None:
        self.__brand = brand

    @property
    def model(self) -> str:
        return self.__model

    @model.setter
    def model(self, model: str) -> None:
        self.__model = model

    @property
    def year(self) -> int:
        return self.__year

    @year.setter
    def year(self, year: int) -> None:
        self.__year = year

    @property
    def speed(self) -> int:
        return self.__speed

    @speed.setter
    def speed(self, speed=0) -> None:
        self.__speed = speed

    def increase_speed(self) -> None:
        self.__speed += 5

    def reduce_speed(self) -> None:
        self.__speed -= 5

    def stop(self) -> None:
        self.__speed = 0

    def speed_display(self) -> None:
        print(f"Текущая скорость: {self.__speed}")

    def reversal(self) -> None:
        self.__speed *= -1


if __name__ == "__main__":
    car = Car("Ferrari", "F355", 1994, 300)
    print(car.brand, car.model, car.year)
    car.reduce_speed()
    car.speed_display()
    car.stop()
    car.increase_speed()
    car.increase_speed()
    car.increase_speed()
    car.speed_display()
    car.reversal()
    car.speed_display()
    print(car.speed)
