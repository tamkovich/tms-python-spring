# Даны три слова. Выяснить, является ли хоть одно из них палиндромом
# ("перевертышем"), т. е. таким, которое читается одинаково слева направо и
# справа налево. (Определить функцию, позволяющую распознавать слова палиндромы.)

from functions import polindr
words = ['matreshka', 'rotator', 'babushka']
[polindr(n) for n in words]
