"""
Создать пять классов описывающие реальные объекты. Каждый класс
должен содержать минимум три приватных атрибута, конструктор, геттеры
и сеттеры для каждого атрибута, два метода.

"""

"""
Клас прямоугольника:
name - названия фигуры
a - длина прямоугольника
b - ширина прямоугольника
"""


class FunSquare:
    def __init__(self, name: str, a: float, b: float) -> None:
        self.__name = name
        self.__a = a
        self.__b = b

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @property
    def a(self) -> float:
        return self.__a

    @a.setter
    def a(self, a: float) -> None:
        self.__a = a

    @property
    def b(self) -> float:
        return self.__b

    @b.setter
    def b(self, b: float) -> None:
        self.__b = b

    """
    функция площадь прямоугольника
    """
    def area(self, a: float, b: float) -> float:
        return a * b

    """
    функция периметр прямоугольника
    """
    def perimeter(self, a: float, b: float) -> float:
        return 2 * (a + b)


"""
Класс Цилиндра:
name - названия фигуры
r - радиус цилиндра
h - высота цилиндра
"""


class FunCylinder:
    def __init__(self, name: str, r: float, h: float) -> None:
        self.__name = name
        self.__r = r
        self.__h = h

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @property
    def r(self) -> float:
        return self.__r

    @r.setter
    def r(self, r: float) -> None:
        self.__r = r

    @property
    def h(self) -> float:
        return self.__h

    @h.setter
    def h(self, h: float) -> None:
        self.__h = h

    """
    Нахождения площадь цилиндра
    """
    def area(self, r: float, h: float) -> float:
        return 2 * r * r * 3.14 + 2 * r * h * 3.14

    """
    Нахождения объем цилиндра
    """
    def volume(self, r: float) -> float:
        return r * r * 3.14


"""
Клссс Трапеция:
name - названия фигуры
a - первая сторона
b - вторая сторона
h - высота трапеции
"""


class FunTrapezoid:
    def __init__(self, name: str, a: float, b: float, h: float) -> None:
        self.__name = name
        self.__a = a
        self.__b = b
        self.__h = h

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @property
    def a(self) -> float:
        return self.__a

    @a.setter
    def a(self, a: float) -> None:
        self.__a = a

    @property
    def b(self) -> float:
        return self.__b

    @b.setter
    def b(self, b: float) -> None:
        self.__b = b

    @property
    def h(self) -> float:
        return self.__h

    @h.setter
    def h(self, h: float) -> None:
        self.__h = h

    """
    Площадь трапеции
    """
    def area(self, a: float, b: float, h: float) -> float:
        return (h * (a + b)) / 2

    """
    Нахождении середини линии трапеции
    """
    def middle_line(self, a: float, b: float) -> float:
        return (a + b) / 2


"""
Класс треугольник:
name - названия фигуры
a - первая сторона
b - вторая сторона
c - третья сторона
"""


class FunTriangle:
    def __init__(self, name: str, a: float, b: float, c: float) -> None:
        self.__name = name
        self.__a = a
        self.__b = b
        self.__c = c

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @property
    def a(self) -> float:
        return self.__a

    @a.setter
    def a(self, a: float) -> None:
        self.__a = a

    @property
    def b(self) -> float:
        return self.__b

    @b.setter
    def b(self, b: float) -> None:
        self.__b = b

    @property
    def c(self) -> float:
        return self.__c

    @c.setter
    def c(self, c: float) -> None:
        self.__c = c

    """
    Нахождения площадь треугольника
    """
    def area(self, a: float, b: float, c: float, p: float) -> float:
        return (p * (p - a) * (p - b) * (p - c)) ** 1 / 2

    """
    Нахождения периметра треугольника
    """
    def perimeter(self, a: float, b: float, c: float) -> float:
        return (a + b + c) / 2


"""
Класс Ромба:
name - назвнии фигры
a - сторона ромба
h - высота рома
"""


class FunRhombus:
    def __init__(self, name: str, a: float, h: float) -> None:
        self.__name = name
        self.__a = a
        self.__h = h

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @property
    def a(self) -> float:
        return self.__a

    @a.setter
    def a(self, a: float) -> None:
        self.__a = a

    @property
    def h(self) -> float:
        return self.__h

    @h.setter
    def h(self, h: float) -> None:
        self.__h = h

    """
    Нахождения площадь ромба
    """
    def area(self, a: float, h: float) -> float:
        return a * h

    """
    Периметр ромба
    """
    def perimeter(self, a: float) -> float:
        return 4 * a


square = FunSquare("parallelogram", 6, 12)
print(square.name)
print(f"parallelogram area = {square.area(square.a, square.b)}")
print(f"parallelogram perimeter = {square.perimeter(square.a, square.b)}")
print("**************")
cylinder = FunCylinder("cylinder", 6, 12)
print(cylinder.name)
print(f"cylinder area = {cylinder.area(cylinder.r, cylinder.h)}")
print(f"cylinder volume = {cylinder.volume(cylinder.r)}")
print("**************")
trapezoid = FunTrapezoid("trapezoid", 6, 12, 8)
print(trapezoid.name)
print(f"trapezoid area = {trapezoid.area(trapezoid.a, trapezoid.b, trapezoid.h)}")
print(f"trapezoid middle_line = {trapezoid.middle_line(trapezoid.a, trapezoid.b)}")
print("**************")
triangle = FunTriangle("triangle", 6, 12, 8)
print(triangle.name)
p = triangle.perimeter(triangle.a, triangle.b, triangle.c)
print(f"triangle area = {triangle.area(triangle.a, triangle.b, triangle.c, p)}")
print(f"triangle perimeter = {p}")
print("**************")
rhombus = FunRhombus("rhombus", 6, 8)
print(rhombus.name)
print(f"rhombus area = {rhombus.area(rhombus.a, rhombus.h)}")
print(f"rhombus perimeter = {rhombus.perimeter(rhombus.a)}")
