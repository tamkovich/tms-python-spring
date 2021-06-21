"""
    Создамем пять классов с 3-я приватными атрибутами
    и миниму двумя методами(дданные методы будут getter, setter
    и конструктор
"""


class car:
    # Конструктор
    def __init__(self, name: str, year: int, price: float):
        self.__name = name
        self.__year = year
        self.__price = price

    # getter он является методам класса
    @property
    def name(self):
        return self.__name

    # setter он является методам класса
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year: int):
        self.__year = year

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price: float):
        self.__price = price


class notebook:
    # Конструктор
    def __init__(self, name: str, model: str, price: float):
        self.__name = name
        self.__model = model
        self.__price = price

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
    def model(self, model: str):
        self.__model = model

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price: float):
        self.__price = price


class book:
    # Конструктор
    def __init__(self, name: str, author: str, price: float):
        self.__name = name
        self.__author = author
        self.__price = price

    # getter он является методам класса
    @property
    def name(self):
        return self.__name

    # setter он является методам класса
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price: float):
        self.__price = price


class phone:
    # Конструктор
    def __init__(self, name: str, numbers: int, model: str):
        self.__name = name
        self.__numbers = numbers
        self.__model = model

    # getter он является методам класса
    @property
    def name(self):
        return self.__name

    # setter он является методам класса
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def numbers(self):
        return self.__numbers

    @numbers.setter
    def numbers(self, numbers: int):
        self.__numbers = numbers

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model: str):
        self.__model = model


class pen:
    # Конструктор
    def __init__(self, color: str, modle: str, price: float):
        self.__color = color
        self.__modle = modle
        self.__price = price

    # getter он является методам класса
    @property
    def color(self):
        return self.__color

    # setter он является методам класса
    @color.setter
    def color(self, color):
        self.__color = color

    @property
    def modle(self):
        return self.__modle

    @modle.setter
    def modle(self, modle: str):
        self.__modle = modle

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price: float):
        self.__price = price


"""
    создаем обьекты классов задаем значение атрибутов
    через конструктор при помощи getter и setter
    меняем значение атрибутов
"""
BMW = car("BMW-m5-e39", 2001, 5500.50)
print(BMW.name, BMW.year, BMW.price)
BMW.name = "BMW-m5-e60"
BMW.year = 2005
BMW.price = 10000.0
print(BMW.name, BMW.year, BMW.price)

lenovo = notebook("YOGA", "tab-4", 1500.20)
print(lenovo.name, lenovo.model, lenovo.price)
lenovo.name = "Gamng_pro"
lenovo.model = "model_v.4"
lenovo.price = 2150.11
print(lenovo.name, lenovo.model, lenovo.price)

book_1 = book("Мастер и маргарита", "Михаил Афанасиевич Булгаков", 200.00)
print(book_1.name, book_1.author, book_1.price)
book_1.name = "Азбука"
book_1.author = "Лев Николаевич Толстой"
book_1.price = 20.00
print(book_1.name, book_1.author, book_1.price)

mi = phone("XAOMI", 379299379992, "redmi 7 pro")
print(mi.name, mi.numbers, mi.model)
mi.name = "MI"
mi.numbers = 911
mi.model = "redmi 4X"
print(mi.name, mi.numbers, mi.model)

pen_ = pen("green", "1", 2)
print(pen_.color, pen_.modle, pen_.price)
pen_.color = "red"
pen_.modle = "1"
pen_.price = 1.5
