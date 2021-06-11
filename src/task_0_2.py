# Задание 2.02
"""Создать два списка произвольного содержания.
Добавить к каждому списку по одному элементу в конец и в начало.
Расширить первый список вторым.
Все изменения выводить на экран"""

cars = ['mers', 'audi', 'bmw']
students = ['ihor', 'masha', 'sasha']
cars.append('ford')
print(cars)

cars.insert(0, 'fiat')
print(cars)

students.append('ivan')
print(students)

students.insert(0, 'gosha')
print(students)

cars.extend(students)
print(cars)
