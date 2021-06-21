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


class fun_square:
    def __init__(self, name, a, b):
        self.__name = name
        self.__a = a
        self.__b = b

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, a):
        self.__a = a

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, b):
        self.__b = b

    # функция площадь прямоугольника
    def area(self, a, b):
        return a * b

    # функция периметр прямоугольника
    def perimeter(self, a, b):
        return 2 * (a + b)


"""
Класс Цилиндра:
name - названия фигуры
r - радиус цилиндра
h - высота цилиндра
"""


class fun_cylinder:
    def __init__(self, name, r, h):
        self.__name = name
        self.__r = r
        self.__h = h

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def r(self):
        return self.__r

    @r.setter
    def r(self, r):
        self.__r = r

    @property
    def h(self):
        return self.__h

    @h.setter
    def h(self, h):
        self.__h = h

    # Нахождения площадь цилиндра
    def area(self, r, h):
        return 2 * r * r * 3.14 + 2 * r * h * 3.14

    # Нахождения объем цилиндра
    def volume(self, r):
        return r * r * 3.14


"""
Клссс Трапеция:
name - названия фигуры
a - первая сторона
b - вторая сторона
h - высота трапеции
"""


class fun_trapezoid:
    def __init__(self, name, a, b, h):
        self.__name = name
        self.__a = a
        self.__b = b
        self.__h = h

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, a):
        self.__a = a

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, b):
        self.__b = b

    @property
    def h(self):
        return self.__h

    @h.setter
    def h(self, h):
        self.__h = h

    # Площадь трапеции
    def area(self, a, b, h):
        return (h * (a + b)) / 2

    #  Нахождении середини линии трапеции
    def middle_line(self, a, b):
        return (a + b) / 2


"""
Класс треугольник:
name - названия фигуры
a - первая сторона
b - вторая сторона
c - третья сторона
"""


class fun_triangle:
    def __init__(self, name, a, b, c):
        self.__name = name
        self.__a = a
        self.__b = b
        self.__c = c

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, a):
        self.__a = a

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, b):
        self.__b = b

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, c):
        self.__c = c

    # Нахождения площадь треугольника
    def area(self, a, b, c, p):
        return (p * (p - a) * (p - b) * (p - c)) ** 1 / 2

    # Нахождения периметра треугольника
    def perimeter(self, a, b, c):
        return (a + b + c) / 2


"""
Класс Ромба:
name - назвнии фигры
a - сторона ромба
h - высота рома
"""


class fun_rhombus:
    def __init__(self, name, a, h):
        self.__name = name
        self.__a = a
        self.__h = h

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, a):
        self.__a = a

    @property
    def h(self):
        return self.__h

    @h.setter
    def h(self, h):
        self.__h = h

    # Нахождения площадь ромба
    def area(self, a, h):
        return a * h

    # Периметр ромба
    def perimeter(self, a):
        return 4 * a


square = fun_square("parallelogram", 6, 12)
print(square.name)
print(f"parallelogram area = {square.area(square.a, square.b)}")
print(f"parallelogram perimeter = {square.perimeter(square.a, square.b)}")
print("**************")
cylinder = fun_cylinder("cylinder", 6, 12)
print(cylinder.name)
print(f"cylinder area = {cylinder.area(cylinder.r, cylinder.h)}")
print(f"cylinder volume = {cylinder.volume(cylinder.r)}")
print("**************")
trapezoid = fun_trapezoid("trapezoid", 6, 12, 8)
print(trapezoid.name)
print(f"trapezoid area = {trapezoid.area(trapezoid.a, trapezoid.b, trapezoid.h)}")
print(f"trapezoid middle_line = {trapezoid.middle_line(trapezoid.a, trapezoid.b)}")
print("**************")
triangle = fun_triangle("triangle", 6, 12, 8)
print(triangle.name)
p = triangle.perimeter(triangle.a, triangle.b, triangle.c)
print(f"triangle area = {triangle.area(triangle.a, triangle.b, triangle.c, p)}")
print(f"triangle perimeter = {p}")
print("**************")
rhombus = fun_rhombus("rhombus", 6, 8)
print(rhombus.name)
print(f"rhombus area = {rhombus.area(rhombus.a, rhombus.h)}")
print(f"rhombus perimeter = {rhombus.perimeter(rhombus.a)}")
