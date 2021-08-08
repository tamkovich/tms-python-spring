""" Создать пять классов описывающие реальные объекты. Каждый класс
должен содержать минимум три приватных атрибута, конструктор, геттеры
и сеттеры для каждого атрибута, два метода. """


class Vegetables:
    def __init__(self, name, packing, weight):
        self.__name = name
        self.__packing = packing
        self.__weight = weight

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def packing(self):
        return self.__packing

    @packing.setter
    def packing(self, packing):
        self.__packing = packing

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.__weight = weight

    def manufacturer_1(self):
        print("Made in Belarus")

    def manufacturer_2(self):
        print("Made in China")


tomat = Vegetables("cherie", "paper bag", 1)
print(f"tomat {tomat.name}, packing - {tomat.packing}, weight = {tomat.weight} kg")
tomat.manufacturer_1()
print("=================================")


class Table:
    def __init__(self, brend, color, price):
        self.__brend = brend
        self.__color = color
        self.price = price

    @property
    def brend(self):
        return self.__brend

    @brend.setter
    def brend(self, brend):
        self.__brend = brend

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

    def shape(self):
        print("square")

    def five(self):
        print("metod_five")


table = Table("IKEA", "white", 20)
print(table.brend)
print(table.color)
print(table.price)
table.shape()
print("=================================")


class Dog:
    def __init__(self, breed, age, nickname):
        self.__breed = breed
        self.__age = age
        self.__nickname = nickname

    @property
    def breed(self):
        return self.__breed

    @breed.setter
    def breed(self, breed):
        self.__breed = breed

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def nickname(self):
        return self.__nickname

    @nickname.setter
    def nickname(self, nickname):
        self.__nickname = nickname

    def bark(self):
        print("Rrrrrrr!")

    def run(self):
        print("Run!")


dog = Dog("Samoed", 6, "Ruby")
print(f"dog breed - {dog.breed}, age - {dog.age} years old, nickname - {dog.nickname}")
dog.bark()
print("=================================")


class Telephone:
    def __init__(self, model, thickness, width):
        self.__model = model
        self.__thickness = thickness
        self.__width = width

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        self.__model = model

    @property
    def thickness(self):
        return self.__thickness

    @thickness.setter
    def thickness(self, thickness):
        self.__thickness = thickness

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    def condition(self):
        print("Good condition!")

    def operator(self):
        print("A_1")


telephone = Telephone("Y-7", 0.7, 10)
print(f"telephone: {telephone.model}, thickness = {telephone.thickness}, width = {telephone.width}")
telephone.condition()
print("=================================")


class Computer:
    def __init__(self, laptop, ssd, hdd):
        self.__laptop = laptop
        self.__ssd = ssd
        self.__hdd = hdd

    @property
    def laptop(self):
        return self.__laptop

    @laptop.setter
    def laptop(self, laptop):
        self.__laptop = laptop

    @property
    def ssd(self):
        return self.__ssd

    @ssd.setter
    def ssd(self, ssd):
        self.__ssd = ssd

    @property
    def hdd(self):
        return self.__hdd

    @hdd.setter
    def hdd(self, hdd):
        self.__hdd = hdd

    def lenovo(self):
        print("Lenovo ideapad 320")

    def monitor(self):
        print(15.4)


comp = Computer("laptop_1", "ssd_256_gb", "hdd_1_tb")
print(f"computer: {comp.laptop}, {comp.ssd}, {comp.hdd}")
comp.lenovo()
comp.monitor()
