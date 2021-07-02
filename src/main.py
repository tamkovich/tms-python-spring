from classes import Circle
from classes import Square
from classes import Point
from classes import Triangle


cir = Circle('circle', Point(0, 0), 5)
tr = Triangle('triangle', Point(1, 2), Point(5, 6), Point(3, 1))
sq = Square('square', Point(1, 2), Point(3, 6))
list_of_figure = [cir, tr, sq]
for figure in list_of_figure:
    print(f"Площадь {figure.name_figure} равен: {round(figure.fun_area(), 3)}")
