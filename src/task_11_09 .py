# 11.3. Создать три класса: Dog, Cat, Parrot. Атрибуты каждого класса: name, age, master.
# Каждый класс содержит конструктор и методы: run, jump, birthday(увеличивает age на 1),
# sleep. Класс Parrot имеет дополнительный метод fly. Cat - meow, Dog - bark.
class Dog:
    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def bark(self):
        print("Woof, woof")

    def jump(self):
        print("Jump")

    def run(self):
        print("Run")

    def sleep(self):
        print("Good night!")

    def birthday(self, age=1):
        self.age += age


class Cat:
    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def meow(self):
        print("Meow")

    def jump(self):
        print("Jump")

    def run(self):
        print("Run")

    def sleep(self):
        print("Good night!")

    def birthday(self, age=1):
        self.age += age


class Parrot:
    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def fly(self):
        print("Fly")

    def jump(self):
        print("Jump")

    def run(self):
        print("Run")

    def sleep(self):
        print("Good night!")

    def birthday(self, age=1):
        self.age += age


dog = Dog("Ker", 4, "Kombo")
cat = Cat("Murzik", 3, "Carap")
parrot = Parrot("Kesha", 1, "Kus")
dog.bark()
dog.jump()
cat.meow()
parrot.fly()
dog.birthday()
print(dog.age)
cat.birthday()
print(cat.age)
parrot.birthday()
print(parrot.age)
