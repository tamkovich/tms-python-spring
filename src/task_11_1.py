#  11.1. Создать пять классов описывающие реальные объекты. Каждый класс
# должен содержать минимум три приватных атрибута, конструктор, геттеры
# и сеттеры для каждого атрибута, два метода.
class Car:
    def __init__(self, brand, model, year, speed):
        self.brand = brand
        self.__model = model
        self.__year = year
        self.__speed = speed

    def road(self):
        print("Едет как положено!")

    def remont(self):
        print("Все исправно")

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        self.__model = model

    def get_year(self):
        return self.__year

    def set_year(self):
        return self.__year

    def get_speed(self):
        return self.__speed

    def set_speed(self):
        return self.__speed


car = Car('Mercedes', "S500", 2005, 300)
car.road()
print(car.brand)
print(car.model)


class BMW(Car):
    def __init__(self, model, year, speed):
        self.__model = model
        self.__year = year
        self.__speed = speed

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        self.__model = model

    def get_year(self):
        return self.__year

    def set_year(self):
        return self.__year

    def get_speed(self):
        return self.__speed

    def set_speed(self):
        return self.__speed

    pass


x5 = BMW("E60", 2006, 200)
x5.road()
x5.remont()
x5.model = "E70"
print(x5.model)


class Opel(Car):
    def __init__(self, model, year, speed):
        self.__model = model
        self.__year = year
        self.__speed = speed

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        self.__model = model

    def get_year(self):
        return self.__year

    def set_year(self):
        return self.__year

    def get_speed(self):
        return self.__speed

    def set_speed(self):
        return self.__speed

    pass


insignia = Opel("B", 2008, 190)
insignia.road()
print(insignia.get_speed())


class Person:
    def __init__(self, profession, sex, experience, age):
        self.profession = profession
        self.__sex = sex
        self.__experience = experience
        self.__age = age

    def lihach(self):
        print("Превышаю скорость")

    def home(self):
        print("Едет домой")

    @property
    def sex(self):
        return self.__sex

    @sex.setter
    def sex(self, sex):
        self.__sex = sex

    def get_experience(self):
        return self.__experience

    def set_experience(self):
        return self.__experience

    def get_age(self):
        return self.__age

    def set_age(self):
        return self.__age


Karina = Person("chemist", "female", "2 years", 27)
Karina.lihach()
print(Karina.profession)
print(Karina.get_age())


class Driver(Person):
    def __init__(self, sex, experience, age):
        self.__sex = sex
        self.__experience = experience
        self.__age = age

    @property
    def sex(self):
        return self.__sex

    @sex.setter
    def sex(self, sex):
        self.__sex = sex

    def get_experience(self):
        return self.__experience

    def set_experience(self):
        return self.__experience

    def get_age(self):
        return self.__age

    def set_age(self):
        return self.__age

    pass


Dima = Driver("male", "1 year", 23)
Dima.lihach()
Dima.home()
print(Dima.sex)
print(Dima.get_experience())
