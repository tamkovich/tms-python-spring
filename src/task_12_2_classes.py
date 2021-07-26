"""
Homework - 12
task_12_2_classes: Создать класс Point, описывающий точку(атрибуты: x, y).
Создать класс Figure. Создать три дочерних класса Circle(атрибуты: координаты
центра(тип Point), длина радиуса; методы: нахождение периметра и площади окружности),
Triangle(атрибуты: три точки, методы: нахождение площади и периметра),
Square(атрибуты: две точки, методы: нахождение площади и периметра).
При потребности создавать все необходимые методы не описанные в задании.
Создать список фигур и в цикле подсчитать и вывести площади всех фигур на экран
[my-oop-03]
Примечание: в рамках задание создать два файла: classes.py и main.py .
В первом будут описаны все классы, во втором классы будут
импортированы и использованы.
"""
from math import pi


class Point:
    """Класс точки, описывающий в атрибутах ее координаты x и y"""
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


class Figure:
    """Класс фигуры с пустыми атрибутами и методами площади и периметра"""
    def __init__(self, area_a=None, perimeter_a=None) -> None:
        self.area_a = area_a
        self.perimeter_a = perimeter_a

    def area_m(self) -> None:
        pass

    def perimeter_m(self) -> None:
        pass


class Circle(Figure):
    """Класс круг с доп. атрибутами и переопределенными методами площади и периметра"""
    def __init__(self, a: Point, r):
        super().__init__(Figure)
        self.a = a
        self.r = r

    def perimeter_m(self) -> None:
        p = 2 * pi * self.r
        self.perimeter_a = p

    def area_m(self) -> None:
        s = pi * self.r ** 2
        self.area_a = s


class Triangle(Figure):
    """Класс треугольник с доп. атрибутами и переопределенными методами площади и периметра"""
    def __init__(self, a: Point, b: Point, c: Point) -> None:
        super().__init__(Figure)
        self.a = a
        self.b = b
        self.c = c
        self.ab = ((self.b.x - self.a.x)**2 + (self.b.y - self.a.y)**2)**0.5
        self.ac = ((self.c.x - self.a.x) ** 2 + (self.c.y - self.a.y) ** 2) ** 0.5
        self.bc = ((self.c.x - self.b.x) ** 2 + (self.c.y - self.b.y) ** 2) ** 0.5

    def area_m(self) -> None:
        pp = (self.ab + self.ac + self.bc)/2
        s = (pp * (pp - self.ab) * (pp - self.ac) * (pp - self.bc))**0.5
        self.area_a = s

    def perimeter_m(self) -> None:
        p = self.ab + self.ac + self.bc
        self.perimeter_a = p


class Square(Figure):
    """Класс квадрат с доп. атрибутами и переопределенными методами площади и периметра"""
    def __init__(self, a: Point, b: Point) -> None:
        super().__init__(Figure)
        self.a = a
        self.b = b
        self.side = (((self.b.x - self.a.x)**2 + (self.b.y - self.a.y)**2)**0.5) / (2 ** 0.5)

    def area_m(self) -> None:
        s = self.side * self.side
        self.area_a = s

    def perimeter_m(self) -> None:
        p = 4 * self.side
        self.perimeter_a = p


if __name__ == "__main__":
    a = Point(3, 3)
    b = Point(8, 12)
    c = Point(18, 7)
    d = Point(0, 0)
    my_circle = Circle(c, 10)
    my_circle.area_m()
    my_circle.perimeter_m()
    print(f"Площадь круга: {my_circle.area_a}")
    print(f"Периметр круга {my_circle.perimeter_a}")
    my_triangle = Triangle(a, b, c)
    my_triangle.area_m()
    my_triangle.perimeter_m()
    print(f"Стороны треугольника: {my_triangle.ab}, {my_triangle.ac}, {my_triangle.bc}")
    print(f"Площадь треугольника: {my_triangle.area_a}")
    print(f"Периметр треугольника {my_triangle.perimeter_a}")
    my_square = Square(a, d)
    my_square.area_m()
    my_square.perimeter_m()
    print(f"Сторона квадрата: {my_square.side}")
    print(f"Площадь квадрата: {my_square.area_a}")
    print(f"Периметр квадрата {my_square.perimeter_a}")

# Денис, по выполнению возникли вопросы (прокомментируй их пожалуйста при review):
# 1. Какой писать тип данных для a, b, c (Point или "Point")?
# 2. Нужно ли для вычисления расстояния между точками делать отдельный метод в классе Figure,
#    ну и стороны у квадрата (решение явно получится более громоздки)?
# 3. Как сделать, чтобы методы area_m и perimeter_m вызывались сразу при создании нового
#    экземпляра класса и сразу же записывались соответствующие атрибуты площади и периметра?
# 4. Суть ошибки "Shadows name 'a' from outer scope", я так понимаю в посторении имен переменных
#    внутри и вне класса? Обязательно ли от нее уходить, если так удобнее понимать код?
# 5. Возможно будут другие предложения по оптимизации кода?
