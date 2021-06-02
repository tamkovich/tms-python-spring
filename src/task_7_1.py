NAME_CONVERT = [
    "дюймы в сантиметры",
    "сантиметры в дюймы",
    "мили в километры",
    "километры в мили",
    "футы в килограммы",
    "килограммы в футы",
    "унции в граммы",
    "граммы в унции",
    "галоны в литры",
    "литры в галоны",
    "пинты в литры",
    "литры в пинты",
]


def dum_sm(dum):
    return dum * 2.54, "сантиметр"


def sm_dum(sm):
    return sm / 2.54, "дюйм"


def mile_kilometr(mile):
    return mile * 1.61, "километр"


def kilometr_mile(kilometr):
    return kilometr / 1.61, "миля"


def fut_kilogramm(fut):
    return fut * 0.4535923745, "килограмм"


def kilogramm_fut(kilogramm):
    return kilogramm / 0.4535923745, "фут"


def uncii_gramm(uncii):
    return uncii * 28.35, "грамм"


def gramm_uncii(gramm):
    return gramm / 28.35, "унция"


def galon_litr(galon):
    return galon * 4.55, "литр"


def litr_galon(litr):
    return litr / 4.55, "галон"


def pinta_litr(pinta):
    return pinta / 0.57, "пинта"


def litr_pinta(litr):
    return litr * 0.57, "литр"


while True:
    print("Программа конвиртирует значение из списка")
    for index, value in enumerate(NAME_CONVERT, 1):
        print(index, value)
    print("0 Выход")
    print("Выберите конвертацию", end=" ")
    check = int(input())
    if check == 1:
        print("Введие значение", end=" ")
        print(dum_sm(int(input())))
        input()
    elif check == 2:
        print("Введие значение", end=" ")
        print(sm_dum(int(input())))
        input()
    elif check == 3:
        print("Введие значение", end=" ")
        print(mile_kilometr(int(input())))
        input()
    elif check == 4:
        print("Введие значение", end=" ")
        print(kilometr_mile(int(input())))
        input()
    elif check == 5:
        print("Введие значение", end=" ")
        print(fut_kilogramm(int(input())))
        input()
    elif check == 6:
        print("Введие значение", end=" ")
        print(kilogramm_fut(int(input())))
        input()
    elif check == 7:
        print("Введие значение", end=" ")
        print(uncii_gramm(int(input())))
        input()
    elif check == 8:
        print("Введие значение", end=" ")
        print(gramm_uncii(int(input())))
        input()
    elif check == 9:
        print("Введие значение", end=" ")
        print(galon_litr(int(input())))
        input()
    elif check == 10:
        print("Введие значение", end=" ")
        print(litr_galon(int(input())))
        input()
    elif check == 11:
        print("Введие значение", end=" ")
        print(pinta_litr(int(input())))
        input()
    elif check == 12:
        print("Введие значение", end=" ")
        print(litr_pinta(int(input())))
        input()
    elif check == 0:
        print("Завершение прогамы")
        break
    else:
        print("Вы ввели не верное значение")
