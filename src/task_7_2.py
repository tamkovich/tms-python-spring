"""
Написать программу, со следующим интерфейсом: пользователю предоставляется на
выбор 12 вариантов перевода(описанных в первой задаче). Пользователь вводит цифру
от одного до двенадцати. После программа запрашивает ввести численное значение.
Затем программа выдает конвертированный результат. Использовать функции из первого
задания. Программа должна быть в бесконечном цикле. Код выхода из программы - 0.
"""
from task_7_1 import inch_in_sant, sant_in_inch, mille_in_kilometr, kilometr_in_mille, funt_in_kg, \
kg_in_funt, uncia_in_gramm, gramm_in_uncia, gallon_in_litr, litr_in_gallon,\
pint_in_litr, litr_in_pinta
while True:
    i = int(input('Введите номер перевода:'))
    a = int(input('Введите значение:'))
    if i == 1:
        inch_in_sant(a)
    elif i == 2:
        sant_in_inch(a)
    elif i == 3:
        mille_in_kilometr(a)
    elif i == 4:
        kilometr_in_mille(a)
    elif i == 5:
        funt_in_kg(a)
    elif i == 6:
        kg_in_funt(a)
    elif i == 7:
        uncia_in_gramm(a)
    elif i == 8:
        gramm_in_uncia(a)
    elif i == 9:
        gallon_in_litr(a)
    elif i == 10:
        litr_in_gallon(a)
    elif i == 11:
        pint_in_litr(a)
    elif i == 12:
        litr_in_pinta(a)
    if i == 0:
        break
