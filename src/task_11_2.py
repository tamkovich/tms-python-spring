# 11.2. Создать класс Car. Атрибуты: марка, модель,
# год выпуска, скорость(по умолчанию 0). Методы: увеличить скорости(скорость + 5), уменьшение скорости(скорость - 5),
# стоп(сброс скорости на 0), отображение скорости, разворот(изменение знака скорости). Все атрибуты приватные.
class Car:
    def __init__(self, brand, model, year, speed):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__speed = speed

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed):
        self.__speed = speed

    def speed_higher(self):
        self.__speed += 5
        print(self.speed)

    def speed_lower(self):
        self.__speed -= 5
        print(self.speed)

    def stop(self):
        self.__speed = 0
        print('Машина остановлена')

    def my_speed(self):
        print('Скорость: ', self.speed)

    def reverse(self):
        self.__speed *= -1
        print('Разворот: ', self.speed)


car = Car('Mercedes', "S500", 2005, 300)
print(car.speed)
car.speed_higher()
car.speed_lower()
car.my_speed()
car.reverse()
car.stop()
