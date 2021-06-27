from classes import Point, Triangle, Square, Circle

circle1 = Circle(Point(1, 2), Point(10, 15))

triangle1 = Triangle(Point(0, 0), Point(0, 3), Point(4, 0))

triangle2 = Triangle(Point(0, 0), Point(0, 3), Point(4, -2))

square1 = Square(Point(1, 2), Point(3, 8))

figures = [circle1, triangle1, triangle2, square1]
for i in figures:
    print(i)
    print(i.find_an_area())
