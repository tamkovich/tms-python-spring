"""
Homework - 11
task_11_1: Создать пять классов описывающие реальные объекты. Каждый класс
должен содержать минимум три приватных атрибута, конструктор, геттеры
и сеттеры для каждого атрибута, два метода.
"""


class Man:
    """Класс мужчины - пьют пиво, трамбуют диван, стареют"""
    def __init__(self, name: str, last_name: str, age: int) -> None:
        self.__name = name
        self.__last_name = last_name
        self.__age = age

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @property
    def last_name(self) -> str:
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name: str) -> None:
        self.__last_name = last_name

    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, age: int) -> None:
        self.__age = age

    def drink_beer(self) -> None:
        print("Немецкое, 3 бокала, хорошо!")

    def lay_sofa(self) -> None:
        print("Хорошо лежиться! А где мой пульт?")

    def get_old(self) -> None:
        self.age += 1


class Women:
    """Класс Женщины - хорошеют, иногда варят борщ"""
    def __init__(self, name: str, last_name: str, eye_size: int) -> None:
        self.__name = name
        self.__last_name = last_name
        self.__eye_size = eye_size

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @property
    def last_name(self) -> str:
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name: str) -> None:
        self.__last_name = last_name

    @property
    def eye_size(self) -> int:
        return self.__eye_size

    @eye_size.setter
    def eye_size(self, eye_size: int) -> None:
        self.__eye_size = eye_size

    def become_beautiful(self) -> None:
        print("Мммм, как же я хогоша, что бы еще подкачать!")

    def cook_borscht_sometimes(self) -> None:
        print("Что-то кушать зочется, не сварить ли борщеца?!")


class Pen:
    """Класс ручки - пишут, иногда текут"""
    def __init__(self, model: str, size: float, color: str) -> None:
        self.__model = model
        self.__size = size
        self.__color = color

    @property
    def model(self) -> str:
        return self.__model

    @model.setter
    def model(self, model: str) -> None:
        self.__model = model

    @property
    def size(self) -> float:
        return self.__size

    @size.setter
    def size(self, size: float) -> None:
        self.__size = size

    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str) -> None:
        self.__color = color

    def write(self) -> None:
        print("Мой дядя, самых честных правил...")

    def flow_sometimes(self) -> None:
        print("Вот, блин, опять потекла!")


class TreeLeaf:
    """Класс лист дерева - вырабатывает О2, падает"""
    def __init__(self, breed: str, size: float, color: str) -> None:
        self.__breed = breed
        self.__size = size
        self.__color = color

    @property
    def breed(self) -> str:
        return self.__breed

    @breed.setter
    def breed(self, breed: str) -> None:
        self.__breed = breed

    @property
    def size(self) -> float:
        return self.__size

    @size.setter
    def size(self, size: float) -> None:
        self.__size = size

    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str) -> None:
        self.__color = color

    def photosynthesis(self) -> None:
        print("Производим кислород!")

    def fall(self) -> None:
        print("Пришла весна, полетели падать!")


class Book:
    """Класс книга - дает информацию или служит подставкой под монитор"""
    def __init__(self, author: str, title: str, age_readers: int) -> None:
        self.__author = author
        self.__title = title
        self.__age_readers = age_readers

    @property
    def author(self) -> str:
        return self.__author

    @author.setter
    def author(self, author: str) -> None:
        self.__author = author

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str) -> None:
        self.__title = title

    @property
    def age_readers(self) -> int:
        return self.__age_readers

    @age_readers.setter
    def age_readers(self, age_readers: int) -> None:
        self.__age_readers = age_readers

    def give_information(self) -> None:
        print("Мммм, какая интересная книга!")

    def monitor_stand(self) -> None:
        print("Как бы поднять монитор?! О, какая отличная толстая книга!")


if __name__ == "__main__":
    man1 = Man("Вася", "Пупкин", 38)
    print(man1.name)
    print(man1.age)
    man1.drink_beer()
    man1.lay_sofa()
    man1.get_old()
    print(man1.age)
