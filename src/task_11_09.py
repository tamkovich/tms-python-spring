"""Задание 11.09
Создать три класса: Dog, Cat, Parrot. Атрибуты каждого
класса: name, age, master. Каждый класс содержит
конструктор и методы: run, jump, birthday(увеличивает age
на 1), sleep. Класс Parrot имеет дополнительный метод fly.
Cat - meow, Dog - bark."""


class Dog:
    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def run(self):
        print("Run!")

    def jump(self):
        print("Jump!")

    def birthday(self):
        self.age += 1

    def sleep(self):
        print("WzWzWzWzWz!")

    def bark(self):
        print("Woof!")


class Cat:
    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def run(self):
        print("Run!")

    def jump(self):
        print("Jump!")

    def birthday(self):
        self.age += 1

    def sleep(self):
        print("WzWzWzWzWz!")

    def meow(self):
        print("Myu!")


class Parrot:
    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def run(self):
        print("Run!")

    def jump(self):
        print("Jump!")

    def birthday(self):
        self.age += 1

    def sleep(self):
        print("WzWzWzWzWz!")

    def fly(self):
        print("Kar_Kar!")


if __name__ == "__mail":

    dog = Dog("Rubi", 5, "a_1")
    dog.run()
    dog.jump()
    dog.birthday()
    dog.sleep()
    dog.bark()
    print(dog.name)
    print(dog.age)
    print(dog.master)

    dog = Cat("Marti", 10, "b_2")
    dog.run()
    dog.jump()
    dog.birthday()
    dog.sleep()
    dog.meow()
    print(dog.name)
    print(dog.age)
    print(dog.master)

    dog = Parrot("Kesha", 30, "c_3")
    dog.run()
    dog.jump()
    dog.birthday()
    dog.sleep()
    dog.fly()
    print(dog.name)
    print(dog.age)
    print(dog.master)
