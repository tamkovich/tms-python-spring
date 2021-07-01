# Создать класс Point, описывающий точку(атрибуты: x, y). Создать класс Figure.
# Создать три дочерних класса Circle(атрибуты: координаты центра(тип Point), длина радиуса; методы: нахождение периметра и площади окружности),
# Triangle(атрибуты: три точки, методы: нахождение площади и периметра),
# Square(атрибуты: две точки, методы: нахождение площади и периметра).
# При потребности создавать все необходимые методы не описанные в задании.
# Создать список фигур и в цикле подсчитать и вывести площади всех фигур на экран[my-oop-03]
# Примечание: в рамках задание создать два файла:  classes.py и  main.py  .
import math


class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y


class Figure:
    def __init__(self, *args):
        if len(args) == 3:
            print("На входе 3 значения, значит это треугольник")
            self.point_1 = args[0]
            self.point_2 = args[1]
            self.point_3 = args[2]
        elif len(args) == 1:
            print(f"На входе 1 значение, значит это окружность")
            self.point_1 = args[0]
        elif len(args) == 2:
            print("На входе 2 значения, значит это квадрат")
            self.point_1 = args[0]
            self.point_2 = args[1]


class Triangle(Figure):

    def get_sides(self):
        point_1 = self.point_1
        x1 = point_1.x
        y1 = point_1.y

        point_2 = self.point_2
        x2 = point_2.x
        y2 = point_2.y

        point_3 = self.point_3
        x3 = point_3.x
        y3 = point_3.y

        a = math.sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))
        b = math.sqrt(pow((x3 - x2), 2) + pow((y2 - y1), 2))
        c = math.sqrt(pow((x1 - x3), 2) + pow((y1 - y3), 2))

        sides = [a, b, c]

        return sides

    def get_length(self):
        sides = self.get_sides()
        return (sides[0] + sides[1] + sides[2]) / 2

    def get_sq(self):
        p = self.get_length()
        sides = self.get_sides()
        return math.sqrt(p * (p - sides[0]) * (p - sides[1]) * (p - sides[2]))


class Circle(Figure):
    def __init__(self, radius, *args):
        super().__init__(*args)
        self.radius = radius

    def get_length(self):
        return 2 * math.pi * self.radius

    def get_sq(self):
        return math.pi * self.radius ** 2


class Square(Figure):

    def get_side(self):
        point_1 = self.point_1
        x1 = point_1.x
        y1 = point_1.y

        point_2 = self.point_2
        x2 = point_2.x
        y2 = point_2.y

        return (x2 - x1) ** 0.5 + (y2 - y1) ** 0.5

    def get_length(self):
        a = self.get_side()
        return 4*a

    def get_sq(self):
        a = self.get_side()
        return a**2
