from classes import Circle
from classes import Point
from classes import Square 
from classes import Triangle


"""Circle"""
p = Point(0, 1)
ci = Circle(p, 5)


"""Triangle"""
a = Point(0, 0)
b = Point(2, 4)
c = Point(3, 1)
t = Triangle(a, b, c)


"""Square"""
point_a = Point(0, 1)
point_b = Point(3, 3)
s = Square(point_a, point_b)

list1 = [ci, t, s]
for x in list1:
    print(x.area())
    print(x.perimeter())
