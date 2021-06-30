"""
    Создаем касс Point для создание
    объеков точки
"""


class Point:
    x = 0
    y = 0

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    @property
    def point(self):
        return self.x, self.y

    @point.setter
    def point(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def point(cls, x, y):
        cls.x = x
        cls.y = y
        return cls.x, cls.y


"""Базовый класс для создания фигур"""


class Figure:
    def __init__(self, p=3.14):
        self.p = p

    def dlina_otreka(self, x: Point, y: Point, x1: Point, y2: Point):
        return ((x1 - x) ** 2 + (y2 - y) ** 2) ** 1 / 2


"""Класс создания круга и вычисления площади и периметра"""


class Circle(Figure):
    def __init__(self, midle_x: Point, midle_y: Point, radius: int):
        super().__init__()
        self.midle_x = midle_x
        self.midle_y = midle_y
        self.radius = radius

    @property
    def perimet(self):
        return 2 * self.p * self.radius

    @property
    def area(self):
        return self.p * self.radius ** 2


"""Класс создания треугольника и вычисления площади и периметра"""


class Treangle(Figure):
    def __init__(self, x: Point, y: Point, x1: Point, y1: Point, x2: Point, y2: Point):
        self.x = x
        self.x1 = x1
        self.x2 = x2
        self.y = y
        self.y1 = y1
        self.y2 = y2
        self.storona_1 = super().dlina_otreka(self.x, self.y, self.x1, self.y1)
        self.storona_2 = super().dlina_otreka(self.x1, self.y1, self.x2, self.y2)
        self.storona_3 = super().dlina_otreka(self.x, self.y, self.x2, self.y2)

    @property
    def perimetr(self):
        return self.storona_1 + self.storona_2 + self.storona_3

    @property
    def area(self):
        return (
            self.perimetr
            * (self.perimetr - self.storona_1)
            * (self.perimetr - self.storona_2)
            * (self.perimetr - self.storona_3)
        ) ** 1 / 2


"""Класс создания Квадрата и вычисления площади и периметра"""


class Square(Figure):
    def __init__(self, x: Point, y: Point, x1: Point, y1: Point):
        self.x = x
        self.x1 = x1
        self.y = y
        self.y1 = y1
        self.storona_1 = super().dlina_otreka(self.x, self.y, self.x1, self.y1)

    @property
    def perimetr(self):
        return self.storona_1 * 4

    @property
    def area(self):
        return self.storona_1 ** 2
