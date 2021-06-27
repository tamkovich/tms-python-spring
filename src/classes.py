# Создать класс Point, описывающий точку(атрибуты: x, y). Создать класс
# Figure. Создать три дочерних класса Circle(атрибуты: координаты
# центра(тип Point), длина радиуса; методы: нахождение периметра и
# площади окружности), Triangle(атрибуты: три точки, методы: нахождение
# площади и периметра), Square(атрибуты: две точки, методы: нахождение
# площади и периметра). При потребности создавать все необходимые
# методы не описанные в задании. Создать список фигур и в цикле
# подсчитать и вывести площади всех фигур на экран[my-oop-03]
# Примечание: в рамках задание создать два файла: classes.py и main.py. В
# первом будут описаны все классы, во втором классы будут
# импортированы и использованы.

from abc import ABC
from abc import abstractmethod
import math


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class AbstractFigure(ABC):

    @abstractmethod
    def find_an_area(self):
        pass

    @abstractmethod
    def find_a_perimetr(self):
        pass

    @staticmethod
    def find_two_points_len(point1: "Point", point2: "Point"):
        return math.sqrt((point2.y - point1.y) ** 2 + (point2.x - point1.x) ** 2)


class Circle(AbstractFigure):
    def __init__(self, center: "Point", point_on_circle: "Point" = None, radius: float = None):
        self.center = center
        self.point_on_circle = point_on_circle
        self.radius = radius

    def find_an_area(self):
        if self.radius:
            print(1)
            return math.pi * self.radius ** 2
        else:
            rad = self.find_two_points_len(self.center, self.point_on_circle)
            return math.pi * rad ** 2

    def find_a_perimetr(self):
        if self.radius:
            return math.pi * self.radius * 2
        else:
            rad = self.find_two_points_len(self.center, self.point_on_circle)
            return math.pi * rad * 2

    def __str__(self):
        area = self.find_an_area()
        perimetr = self.find_a_perimetr()
        return f"Circle with square {area} units and lenth {perimetr} units."


class TriangleException(Exception):
    def __init__(self, message='There are no such triangles'):
        super().__init__(message)


class Triangle(AbstractFigure):
    def __init__(self, point1: "Point", point2: "Point", point3: "Point"):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3
        self.side_a = self.find_two_points_len(self.point1, self.point2)
        self.side_b = self.find_two_points_len(self.point3, self.point2)
        self.side_c = self.find_two_points_len(self.point1, self.point3)
        if not(self.side_a + self.side_b > self.side_c and self.side_a + self.side_c > self.side_b and self.side_b + self.side_c > self.side_a):
            raise TriangleException
        self.sides_array = sorted([self.side_a, self.side_b, self.side_c])
        if self.sides_array[0] ** 2 + self.sides_array[1] ** 2 \
                == self.sides_array[2] ** 2:
            self.triangle_property = "Rectangular"
        elif self.side_a == self.side_b == self.side_c:
            self.triangle_property = "Equilateral"
        elif self.side_a == self.side_b or self.side_b \
                == self.side_c or self.side_a == self.side_c:
            self.triangle_property = "Isosceles"
        elif self.sides_array[0] ** 2 + self.sides_array[1] \
                ** 2 < self.sides_array[2] ** 2:
            self.triangle_property = "Obtuse"
        else:
            self.triangle_property = "Acute-angled"

    def find_a_perimetr(self):
        return self.side_a + self.side_b + self.side_c

    def find_an_area(self):
        p = self.find_a_perimetr() / 2
        return math.sqrt(p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c))

    def __str__(self):
        area = self.find_an_area()
        perimetr = self.find_a_perimetr()
        return f"{self.triangle_property} triangle " \
               f"with area {area} units and perimetr {perimetr} units."


class Square(AbstractFigure):
    def __init__(self, point1: "Point", point2: "Point"):
        self.point1 = point1
        self.point2 = point2
        self.side = self.find_two_points_len(self.point1, self.point2)

    def find_a_perimetr(self):
        return self.side * 4

    def find_an_area(self):
        return self.side ** 2

    def __str__(self):
        area = self.find_an_area()
        perimetr = self.find_a_perimetr()
        return f"Square with area {area} units and perimetr {perimetr} units."
