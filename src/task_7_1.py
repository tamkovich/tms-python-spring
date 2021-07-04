def fun_inch(inch):  # Дюймы в сантиметры
    inch *= 2.54
    return inch


def fun_santimetr(santimetr):  # Сантиметры в дюймы
    santimetr *= 0.39
    return santimetr


def fun_milli(milli):  # Мили в километры
    milli *= 1 / 1000000
    return milli


def fun_kilo(kilo):  # Километры в мили
    kilo *= 1000000
    return kilo


def fun_funt(funt):  # Фунты в килограммы
    funt *= 0.45359237
    return funt


def fun_kilogram(kilogram):  # Килограммы в фунты
    kilogram /= 0.45359237
    return kilogram


def fun_unsiya(unsiya):  # Унции в граммы
    unsiya *= 28.3495
    return unsiya


def fun_gramm(gramm):  # Граммы в унции
    gramm *= 0.035274
    return gramm


def fun_galon(galon):  # Галлон в литры
    galon *= 3.785412
    return galon


def fun_litr(litr):  # Литры в галлоны
    litr *= 2.113376
    return litr


def fun_pinti(pint):  # Пинты в литры
    return pint * 0.473176


def fun_litr_pint(litr_pint):  # Литры в пинты
    return litr_pint * 2.11338


while True:
    print("Введите число для перевода: ")
    number = input()
    if number.isdigit():
        list_of_trans = {
            1: fun_inch(int(number)),
            2: fun_santimetr(int(number)),
            3: fun_milli(int(number)),
            4: fun_kilo(int(number)),
            5: fun_funt(int(number)),
            6: fun_kilogram(int(number)),
            7: fun_unsiya(int(number)),
            8: fun_gramm(int(number)),
            9: fun_galon(int(number)),
            10: fun_litr(int(number)),
            11: fun_pinti(int(number)),
            12: fun_litr_pint(int(number))
        }
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
            print(round(list_of_trans[trans], 3))
