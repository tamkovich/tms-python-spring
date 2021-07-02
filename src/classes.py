"""
Создать класс Point, описывающий точку(атрибуты: x, y). Создать класс
Figure. Создать три дочерних класса Circle(атрибуты: координаты
центра(тип Point), длина радиуса; методы: нахождение периметра и
площади окружности), Triangle(атрибуты: три точки, методы: нахождение
площади и периметра), Square(атрибуты: две точки, методы: нахождение
площади и периметра). При потребности создавать все необходимые
методы не описанные в задании. Создать список фигур и в цикле
подсчитать и вывести площади всех фигур на экран[my-oop-03]
Примечание: в рамках задание создать два файла: classes.py и main.py. В
первом будут описаны все классы, во втором классы будут
импортированы и использованы.
"""
from abc import ABC
from abc import abstractmethod


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Figure(ABC):
    @abstractmethod
    def fun_area(self):
        pass

    @abstractmethod
    def fun_perimetr(self):
        pass


class Circle(Figure):
    def __init__(self, name_figure, point: 'Point', len_r):
        self.name_figure = name_figure
        self.point = point
        self.len_r = len_r

    def fun_perimetr(self):
        return 2 * 3.14 * self.len_r

    def fun_area(self):
        return 3.14 * self.len_r ** 2


class Triangle(Figure):
    def __init__(self, name_figure, point1: 'Point', point2: 'Point', point3: 'Point'):
        self.name_figure = name_figure
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3

        # Нахождения площадь треугольника
    def fun_area(self):
        len_a = ((self.point2.x - self.point1.x) ** 2 + (self.point2.y - self.point1.y) ** 2) ** 0.5
        len_b = ((self.point3.x - self.point1.x) ** 2 + (self.point3.y - self.point1.y) ** 2) ** 0.5
        len_c = ((self.point3.x - self.point2.x) ** 2 + (self.point3.y - self.point2.y) ** 2) ** 0.5
        p = (len_a + len_b + len_c) / 2
        return (p * (p - len_a) * (p - len_b) * (p - len_c)) ** 0.5

        # Нахождения периметра треугольника
    def fun_perimetr(self):
        len_a = ((self.point2.x - self.point1.x) ** 2 + (self.point2.y - self.point1.y) ** 2) ** 0.5
        len_b = ((self.point3.x - self.point1.x) ** 2 + (self.point3.y - self.point1.y) ** 2) ** 0.5
        len_c = ((self.point3.x - self.point2.x) ** 2 + (self.point3.y - self.point2.y) ** 2) ** 0.5
        return len_a + len_b + len_c


class Square(Figure):
    def __init__(self, name_figure, point1: 'Point', point2: 'Point'):
        self.name_figure = name_figure
        self.point1 = point1
        self.point2 = point2

    def fun_area(self):
        return ((self.point2.x - self.point1.x) **
                (self.point2.y - self.point1.y))

    def fun_perimetr(self):
        return 2 * ((self.point2.x - self.point1.x) ** (self.point2.y - self.point1.y))
