import math

from fractions import Fraction


a = 5
b = 7

c = math.sqrt((a**2) + (b**2))
print(c)


after_review_c = ((a**2) + (b**2))**0.5
print(after_review_c)


i = Fraction(1, 2)
s = i * a * b
print(float(s))
