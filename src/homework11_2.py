# Создать класс Car. Атрибуты: марка, модель, год выпуска, скорость(по
# умолчанию 0). Методы: увеличить скорости(скорость + 5), уменьшение
# скорости(скорость - 5), стоп(сброс скорости на 0), отображение скорости,
# разворот(изменение знака скорости). Все атрибуты приватные.

class Car:
    def __init__(self, brand, model, year, speed):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__speed = speed

    @property
    def brand(self):
        return self.__brand

    @property
    def model(self):
        return self.__model

    @property
    def year(self):
        return self.__year

    @property
    def speed(self):
        return self.__speed

    def acceleration(self):
        self.__speed += 5
        print('speed increased by 5, now is ', self.speed)

    def braking(self):
        self.__speed -= 5
        print('speed reduced by 5, now is ', self.speed)

    def stop(self):
        self.__speed = 0
        print('You have stopped, your speed is 0')

    def show_speed(self):
        print('speed is ', self.speed)

    def reverse(self):
        self.__speed *= -1
        print('speed now is ', self.speed)


a = Car('Porshe', 'Taycan', '2021', 110)
print(a.speed)
a.braking()
print(a.speed)
a.reverse()
a.show_speed()
