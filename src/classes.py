"""Создать класс Point, описывающий точку(атрибуты: x, y). Создать класс
Figure. Создать три дочерних класса Circle(атрибуты: координаты
центра(тип Point), длина радиуса; методы: нахождение периметра и
площади окружности), Triangle(атрибуты: три точки, методы: нахождение
площади и периметра), Square(атрибуты: две точки, методы: нахождение
площади и периметра). При потребности создавать все необходимые
методы не описанные в задании. Создать список фигур и в цикле
подсчитать и вывести площади всех фигур на экран[my-oop-03]
Примечание: в рамках задание создать два файла: classes.py и main.py. В
первом будут описаны все классы, во втором классы будут
импортированы и использованы"""

from abc import ABC
from abc import abstractmethod
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class AbstractFigure(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(AbstractFigure):
    def __init__(self, center: Point, radius):
        self.center = center
        self.radius = radius

    def perimeter(self):
        return f'Периметр круга равен {2 * math.pi * self.radius}'

    def area(self):
        return f'Площадь круга равна {math.pi * self.radius ** 2}'


class Triangle(AbstractFigure):
    def __init__(self, a=Point, b=Point, c=Point):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        length_ab = ((self.b.x - self.a.x) ** 2 + (self.b.y - self.a.y) ** 2) ** 0.5
        length_ac = ((self.c.x - self.a.x) ** 2 + (self.c.y - self.a.y) ** 2) ** 0.5
        length_bc = ((self.c.x - self.b.x) ** 2 + (self.c.y - self.b.y) ** 2) ** 0.5
        return f'Периметр треугольника равен {length_bc + length_ac + length_ab}'

    def area(self):
        length_ab = ((self.b.x - self.a.x) ** 2 + (self.b.y - self.a.y) ** 2) ** 0.5
        length_ac = ((self.c.x - self.a.x) ** 2 + (self.c.y - self.a.y) ** 2) ** 0.5
        length_bc = ((self.c.x - self.b.x) ** 2 + (self.c.y - self.b.y) ** 2) ** 0.5
        p = (length_bc + length_ac + length_ab) / 2
        area = (p * (p - length_ac) * (p - length_bc) * (p - length_ab)) ** 0.5
        return f'Площадь трехугольника равна {area}'


class Square(AbstractFigure):
    def __init__(self, a=Point, b=Point):
        self.a = a
        self.b = b

    def perimeter(self):
        length = ((self.b.x - self.a.x) ** 2 + (self.b.y - self.a.y) ** 2) ** 0.5
        return f'Периметр квадрата равен {length * 4}'

    def area(self):
        length = ((self.b.x - self.a.x) ** 2 + (self.b.y - self.a.y) ** 2) ** 0.5
        return f'Площадь квадрата равна {length ** 2}'
