"""
Дюймы в сантиметры
"""
def fun_inch(inch):
    inch *= 2.54
    return inch


"""
Сантиметры в дюймы
"""
def fun_santimetr(santimetr):
    santimetr *= 0.39
    return santimetr


"""
Мили в километры
"""
def fun_milli(milli):
    milli /=  1000000
    return milli

"""
Километры в мили
"""
def fun_kilo(kilo):
    kilo *= 1000000
    return kilo


"""
Фунты в килограммы
"""
def fun_funt(funt):
    funt *= 0.45359237
    return funt


"""
Килограммы в фунты
"""
def fun_kilogram(kilogram):
    kilogram /= 0.45359237
    return kilogram


"""
Унции в граммы
"""
def fun_unsiya(unsiya):
    unsiya *= 28.3495
    return unsiya


"""
Граммы в унции
"""
def fun_gramm(gramm):
    gramm *= 0.035274
    return gramm


"""
Галлон в литры
"""
def fun_galon(galon):
    galon *= 3.785412
    return galon


"""
Литры в галлоны
"""
def fun_litr(litr):
    litr *= 2.113376
    return litr


"""
Пинты в литры
"""
def fun_pinti(pint):
    return pint * 0.473176


"""
Литры в пинты
"""
def fun_litr_pint(litr_pint):
    return litr_pint * 2.11338


list_of_trans = {
            1: fun_inch,
            2: fun_santimetr,
            3: fun_milli,
            4: fun_kilo,
            5: fun_funt,
            6: fun_kilogram,
            7: fun_unsiya,
            8: fun_gramm,
            9: fun_galon,
            10: fun_litr,
            11: fun_pinti,
            12: fun_litr_pint
        }
while True:
    print("Введите число для перевода: ")
    number = input()
    if number.isdigit():
        print("1. Дюймы в сантиметры")
        print("2. Сантиметры в дюймы")
        print("3. Мили в километры")
        print("4. Километры в мили")
        print("5. Фунты в килограммы")
        print("6. Килограммы в фунты")
        print("7. Унции в граммы")
        print("8. Граммы в унции")
        print("9. Галлон в литры")
        print("10. Литры в галлоны")
        print("11. Пинты в литры")
        print("12. Литры в пинты")
        print("Выберите вариант перевода:  ")
        trans = int(input())
        if trans in list_of_trans:
            print(round(list_of_trans[trans](int(number)), 3))
