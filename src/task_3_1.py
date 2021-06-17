"""Введите число. Если это число делиться на 1000 без остатка, то выведите на
экран "millennium"""
chislo = input("введите число")
if int(chislo) % 1000 == 0:
    print("millennium")