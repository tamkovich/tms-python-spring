""" Создать класс Car. Атрибуты: марка, модель, год выпуска, скорость(по
умолчанию 0). Методы: увеличить скорости(скорость + 5), уменьшение
скорости(скорость - 5), стоп(сброс скорости на 0), отображение скорости,
разворот(изменение знака скорости). Все атрибуты приватные."""


class Car:
    def __init__(self, mark, model, year_of_manufacture, speed):
        self.__mark = mark
        self.__model = model
        self.__year_of_manufacture = year_of_manufacture
        self.speed = speed

    @property
    def mark(self):
        return self.__mark

    @mark.setter
    def mark(self, mark):
        self.__mark = mark

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        self.__model = model

    @property
    def year_of_manufacture(self):
        return self.__year_of_manufacture

    @year_of_manufacture.setter
    def year_of_manufacture(self, year_of_manufacture):
        self.__year_of_manufacture = year_of_manufacture

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed):
        self.__speed = speed

    def increase_speed(self):
        self.__speed += 5
        print(self.speed)

    def reduce_speed(self):
        self.__speed -= 5
        print(self.speed)

    def zero_speed(self):
        self.__speed = 0
        print(self.speed)

    def turn(self):
        self.__speed *= -1
        print(self.speed)


if __name__ == "__main__":
    car = Car("Lada", "2101", "1989", 220)
    print(f"mark - {car.mark}, model - {car.model}, year - {car.year_of_manufacture}, speed - {car.speed}")
    car.increase_speed()
    car.reduce_speed()
    car.turn()
    car.increase_speed()
    car.reduce_speed()
    car.turn()
    car.zero_speed()
    car.increase_speed()
    car.turn()
