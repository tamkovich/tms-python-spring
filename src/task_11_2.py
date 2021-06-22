"""
Создать класс Car. Атрибуты: марка, модель, год выпуска, скорость(по умолчанию 0).
Методы: увеличить скорости(скорость + 5), уменьшение скорости(скорость - 5),
стоп(сброс скорости на 0),
отображение скорости, разворот(изменение знака скорости). Все атрибуты приватные.
"""


class Car:
    def __init__(self, car_brand, model, year, speed=0):
        self.__car_brand = car_brand
        self.__model = model
        self.__year = year
        self.__speed = speed

    def get_speeed(self):
        return self.__speed

    def set_speed(self, speed):
        self.__speed = speed

    """
    Изменение скорости
    """

    def speed_up(self):
        self.__speed += 5

    def speed_down(self):
        self.__speed -= 5

    def stop(self):
        self.__speed = 0

    def reversal(self):
        self.__speed *= -1

    def info_speed(self):
        return f'speed = {self.__speed}'

    def info_car(self):
        return f'{self.__car_brand}\n{self.__model}\n' \
               f'{self.__year}\n{self.__speed}'


"""
Вывод информации объекта и скорости
"""

if __name__ == '__main__':
    car = Car('Tesla', 'Model S', 2019, 55)
    print(car.info_car())
    print(car.info_speed())
    car.speed_up()
    print(car.info_speed())
    car.speed_down()
    print(car.info_speed())
    car.reversal()
    print(car.info_speed())
    car.stop()
    print(car.info_speed())
