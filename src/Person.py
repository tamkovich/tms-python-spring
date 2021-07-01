# Создать пять классов описывающие реальные объекты.
# Каждый класс должен содержать минимум три приватных атрибута,
# конструктор, геттеры и сеттеры для каждого атрибута, два метода.

class Person:
    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def surname(self):
        return self.surname

    @surname.setter
    def surname(self, surname):
        self.__surname = surname

    @property
    def age(self):
        return self.age

    @age.setter
    def age(self, age):
        self.__age = age

    def get_fullname(self):
        return f"{self.__name} {self.__surname}"

    def get_age_category(self):
        if self.__age < 10:
            return "child"
        elif self.__age < 15:
            return "teenager"
        else:
            return "adult"
