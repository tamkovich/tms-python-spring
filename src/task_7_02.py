"""Написать программу для работы с матрицами:
1. Создание
2. Вывод
3. Сумма всех элементов
4. Нахождение максимального элемента
5. Нахождение минимального элемента."""
import random


def matr(n):
    mat = []
    for i in range(n):
        box = []
        for h in range(n):
            box.append(random.randint(1, 20))
        mat.append(box)
    return mat


def max_mat(n):
    ma = []
    for q in matr(n):
        ma.append(max(q))
    ma_max = max(ma)
    return ma_max


def min_mat(n):
    mi = []
    for q in matr(n):
        mi.append(min(q))
    mi_min = min(mi)
    return mi_min


def sum_el_mat(n):
    summ_el = 0
    for q in matr(n):
        for w in q:
            summ_el += w
    return summ_el


def vivod_matr(n):
    print(matr(n))


print(max_mat(6))
print(min_mat(6))
print(sum_el_mat(6))
vivod_matr(6)
