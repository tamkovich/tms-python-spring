"""
    Создаем клас car с атрибутами
    марка, модель, год, скорость
    создаем методы getter and setter
    для атрибутов и задаем три метода
    увелечение скорости уменьшение скорости
    и разворот
"""


class car:
    # Конструктор
    def __init__(self, name: str, model: str, year: int, speed: int = 0):
        self.__name = name
        self.__model = model
        self.__year = year
        self.__speed = speed

    # getter он является методам класса
    @property
    def name(self):
        return self.__name

    # setter он является методам класса
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def model(self):
        return self.__model

    @model.setter
    def price(self, model: str):
        self.__model = model

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year: int):
        self.__year = year

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed: int):
        self.__speed = speed

    # Метод увиличение скорости
    def up_speed(self, up_speed=5):
        self.__speed += up_speed

    # Метод уменьшение скорости
    def down_speed(self, down_speed=5):
        self.__speed -= down_speed

    # Остановка
    def stop_speed(self, stop_speed=0):
        self.__speed = stop_speed

    # Метод разворота
    def reversal(self):
        self.__speed = -(self.__speed)


car_1 = car("audi", "rs6", 2004)
print(car_1.name, car_1.model, car_1.year, car_1.speed)
car_1.up_speed()
print(car_1.speed)
car_1.reversal()
print(car_1.speed)
