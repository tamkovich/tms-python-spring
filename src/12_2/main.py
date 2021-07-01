from classes import Triangle, Point, Circle, Square


def main():
    tr = Triangle(Point(0, 0), Point(2, 2), Point(2, 0))
    circle = Circle(5, Point(0, 0))
    square = Square(Point(0, 0), Point(4, 4))
    fs = [tr, circle, square]
    for f in fs:

        print(f.get_length())
        print(f.get_sq())


if __name__ == '__main__':
    main()
