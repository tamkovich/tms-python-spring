# Дюймы в сантиметры
def fun_inch(inch):
    inch *= 2.54
    return inch
# Сантиметры в дюймы

def fun_santimetr(santimetr):
    santimetr *= 0.39
    return santimetr
# Мили в километры

def fun_milli(milli):
    milli *= 1 / 1000000
    return milli
# Километры в мили

def fun_kilo(kilo):
    kilo *= 1000000
    return kilo
# Фунты в килограммы

def fun_funt(funt):
    funt *= 0.45359237
    return funt
# Килограммы в фунты

def fun_kilogram(kilogram):
    kilogram /= 0.45359237
    return kilogram
# Унции в граммы

def fun_unsiya(unsiya):
    unsiya *= 28.3495
    return unsiya
# Граммы в унции

def fun_gramm(gramm):
    gramm *= 0.035274
    return gramm
# Галлон в литры

def fun_galon(galon):
    galon *= 3.785412
    return galon
# Литры в галлоны

def fun_litr(litr):
    litr *= 2.113376
    return litr
# Пинты в литры

def fun_pinti(pint):
    return pint * 0.473176
# Литры в пинты

def fun_litr_pint(litr_pint):
    return litr_pint * 2.11338

while True:
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
    if trans == 1:
        print("Введите число для перевода: ")
        number = input()
        if number.isdigit():
            print(f"Дюймы в сантиметры: {fun_inch(int(number))}")
    if trans == 2:
        print("Введите число для перевода: ")
        number = input()
        if number.isdigit():
            print(f"Сантиметры в дюймы: {fun_santimetr(int(number))}")
    if trans == 3:
        print("Введите число для перевода: ")
        number = input()
        if number.isdigit():
            print(f"Мили в километры: {fun_milli(int(number))}")
    if trans == 4:
        print("Введите число для перевода: ")
        number = input()
        if number.isdigit():
            print(f"Километры в мили: {fun_kilo(int(number))}")
    if trans == 5:
        print("Введите число для перевода: ")
        number = input()
        if number.isdigit():
            print(f"Фунты в килограммы: {fun_funt(int(number))}")
    if trans == 6:
        print("Введите число для перевода: ")
        number = input()
        if number.isdigit():
            print(f"Килограммы в фунты: {fun_kilogram(int(number))}")
    if trans == 7:
        print("Введите число для перевода: ")
        number = input()
        if number.isdigit():
            print(f"Унции в граммы: {fun_unsiya(int(number))}")
    if trans == 8:
        print("Введите число для перевода: ")
        number = input()
        if number.isdigit():
            print(f"Граммы в унции: {fun_gramm(int(number))}")
    if trans == 9:
        print("Введите число для перевода: ")
        number = input()
        if number.isdigit():
            print(f"Галлон в литры: {fun_galon(int(number))}")
    if trans == 10:
        print("Введите число для перевода: ")
        number = input()
        if number.isdigit():
            print(f"Литры в галлоны: {fun_litr(int(number))}")
    if trans == 11:
        print("Введите число для перевода: ")
        number = input()
        if number.isdigit():
            print(f"Пинты в литры: {fun_pinti(int(number))}")
    if trans == 12:
        print("Введите число для перевода: ")
        number = input()
        if number.isdigit():
            print(f"Литры в пинты: {fun_litr_pint(int(number))}")
    print("Для выхода из программы нажмите на ноль - '0")
    trans = input()
    if trans.isdigit():
        if int(trans) == 0:
            break
