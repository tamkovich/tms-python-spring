"""Задание 12.02.
Создать класс Point, описывающий точку(атрибуты: x, y).
Создать класс Figure.
Создать три дочерних класса:
- Circle(атрибуты: координаты центра(тип Point), длина радиуса;
    методы: нахождение периметра и площади окружности),
- Triangle(атрибуты: три точки, методы: нахождение площади и периметра),
- Square(атрибуты: две точки, методы: нахождение площади и периметра).

(При потребности, создавать все необходимые методы не описанные в задании.)

Создать список фигур и в цикле подсчитать и вывести площади всех фигур на экран
Примечание: в рамках задание создать два файла: classes.py и main.py.
В первом будут описаны все классы, во втором классы будут
импортированы и использованы."""

from classes import Circle
from classes import Point
from classes import Square
from classes import Triangle

figures = [Circle(Point(0, 0), 200),
           Square(Point(100, 100), Point(300, 200)),
           Triangle(Point(50, 0), Point(150, 50), Point(100, 70))]

for figure in figures:
    print(f"{figure}:\n"
          f"  - perimeter {figure.perimeter:.2f}\n"
          f"  - area {figure.area:.2f}\n")
