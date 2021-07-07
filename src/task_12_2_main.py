"""
    Импорируем Созданые классы
"""
from task_12_2_classes import Circle
from task_12_2_classes import Square
from task_12_2_classes import Treangle

"""Создаем экземяры классов"""
circle = Circle(1, 1, 11)
trangle = Treangle(1, 1, 2, 1, 1, 3)
square = Square(1, 1, 2, 2)
print(f"периметр круга равен {circle.perimet}, площадь = {circle.area}")
print(f"периметр круга равен {trangle.perimetr}, площадь = {trangle.area}")
print(f"периметр круга равен {square.perimetr}, площадь = {square.area}")
