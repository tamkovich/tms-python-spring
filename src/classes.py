from abc import ABC
from abc import abstractmethod


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    @classmethod
    def clone(cls, point: 'Point') -> 'Point':
        return cls(point.x, point.y)


class Figure(ABC):
    @abstractmethod
    def perimeter(self) -> float:
        pass

    @abstractmethod
    def area(self) -> float:
        pass

    @staticmethod
    def length_between(point_1: 'Point', point_2: 'Point') -> float:
        return ((point_2.y - point_1.y) ** 2 + (point_2.x - point_1.x) ** 2) ** 0.5


class Circle(Figure):
    def __init__(self, center: 'Point', radius: float):
        self.center = Point.clone(center)
        self.radius = radius

    @property
    def perimeter(self) -> float:
        return 2 * 3.14 * self.radius

    @property
    def area(self) -> float:
        return 3.14 * self.radius ** 2

    def __str__(self):
        return "Circle"


class Triangle(Figure):
    def __init__(self, apex_1: 'Point', apex_2: 'Point', apex_3: 'Point'):
        self.apex_1 = Point.clone(apex_1)
        self.apex_2 = Point.clone(apex_2)
        self.apex_3 = Point.clone(apex_3)

    @property
    def perimeter(self) -> float:
        return Figure.length_between(self.apex_1, self.apex_2)\
            + Figure.length_between(self.apex_2, self.apex_3)\
            + Figure.length_between(self.apex_3, self.apex_1)

    @property
    def area(self) -> float:
        p = self.perimeter / 2
        a = Figure.length_between(self.apex_1, self.apex_2)
        b = Figure.length_between(self.apex_2, self.apex_3)
        c = Figure.length_between(self.apex_3, self.apex_1)
        return (p * (p - a) * (p - b) * (p - c)) ** 0.5

    def __str__(self):
        return "Triangle"


class Square(Figure):
    def __init__(self, apex_1: 'Point', apex_2: 'Point'):
        self.apex_1 = Point.clone(apex_1)
        self.apex_2 = Point.clone(apex_2)

    @property
    def perimeter(self) -> float:
        return 2 * (abs(self.apex_1.x - self.apex_2.x) + abs(self.apex_1.y - self.apex_2.y))

    @property
    def area(self) -> float:
        return abs(self.apex_1.x - self.apex_2.x) * abs(self.apex_1.y - self.apex_2.y)

    def __str__(self):
        return "Square"
