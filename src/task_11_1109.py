"""
Homework - 11
task_11_11.09:
Создать три класса: Dog, Cat, Parrot. Атрибуты каждого класса: name, age, master.
Каждый класс содержит конструктор и методы: run, jump, birthday(увелич. age на 1), sleep.
Класс Parrot имеет дополнительный метод fly. Cat - meow, Dog - bark.
"""


class Dog:
    """ Создан класс в соответствии с условиями задачи"""

    def __init__(self, name: str, age: int, master: str) -> None:
        self.name = name
        self.age = age
        self.master = master

    def run(self) -> None:
        print("Run!")

    def jump(self) -> None:
        print("Jump!")

    def birthday(self) -> None:
        self.age = self.age + 1

    def sleep(self) -> None:
        print("Sleep!")

    def bark(self) -> None:
        print("Гав-гав!")


class Cat:
    """ Создан класс в соответствии с условиями задачи"""

    def __init__(self, name: str, age: int, master: str) -> None:
        self.name = name
        self.age = age
        self.master = master

    def run(self) -> None:
        print("Run!")

    def jump(self) -> None:
        print("Jump!")

    def birthday(self) -> None:
        self.age = self.age + 1

    def sleep(self) -> None:
        print("Sleep!")

    def meow(self) -> None:
        print("Мяяаауу!")


class Parrot:
    """ Создан класс в соответствии с условиями задачи"""

    def __init__(self, name: str, age: int, master: str) -> None:
        self.name = name
        self.age = age
        self.master = master

    def run(self) -> None:
        print("Run!")

    def jump(self) -> None:
        print("Jump!")

    def birthday(self) -> None:
        self.age = self.age + 1

    def sleep(self) -> None:
        print("Sleep!")

    def fly(self) -> None:
        print("Лечууу!")


if __name__ == "__main__":
    dog = Dog("Барбос", 6, "Вася")
    parrot_kesha = Parrot("Кеша", 6, "Таити")
    print(dog.name)
    print(dog.age)
    print(dog.master)
    dog.birthday()
    print(dog.age)
    parrot_kesha.fly()
