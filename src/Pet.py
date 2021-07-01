# Создать пять классов описывающие реальные объекты.
# Каждый класс должен содержать минимум три приватных атрибута,
# конструктор, геттеры и сеттеры для каждого атрибута, два метода.

class Pet:
    def __init__(self, name, breed, age):
        self.__name = name
        self.__breed = breed
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def breed(self):
        return self.breed

    @breed.setter
    def breed(self, breed):
        self.__breed = breed

    @property
    def age(self):
        return self.age

    @age.setter
    def age(self, age):
        self.__age = age

    def get_description(self):
        return f"{self.__name} {self.__age} {self.__breed}"

    def increase_age(self):
        self.__age += 1