"""
Создать класс Car. Атрибуты: марка, модель, год выпуска, скорость(по
умолчанию 0). Методы: увеличить скорости(скорость + 5), уменьшение
скорости(скорость - 5), стоп(сброс скорости на 0), отображение скорости,
разворот(изменение знака скорости). Все атрибуты приватные.
"""
class Car:
    def __init__(self, brand, model, year, speed = 0):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__speed = speed
    @property
    def brand(self):
        return self.__brand
    @brand.setter
    def brand(self, brand):
        self.__brand = brand

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        self.__model = model

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        self.__year = year

    # увеличить скорости(скорость + 5)
    def increase_speed(self, speed):
        self.__speed += speed

    # уменьшение скорости(скорость - 5)
    def decreas_speed(self, speed):
        self.__speed -= speed

    # стоп(сброс скорости на 0)
    def stop_speed(self):
        self.__speed = 0

    # отображение скорости
    def display_speed(self):
        print(f"Скорость машины {self.__brand} равно {self.__speed}")

    # разворот(изменение знака скорости)
    def change_speed(self, speed):
        self.__speed = speed

if __name__ == "__main__":
    car = Car("BMW", "M4", 2020, 120)
    car.display_speed()
    car.increase_speed(5)
    car.display_speed()
    car.decreas_speed(5)
    car.display_speed()
    car.stop_speed()
    car.display_speed()
    car.change_speed(120)
    car.display_speed()
