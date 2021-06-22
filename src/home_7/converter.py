def inches_to_centimeters(inches):
    return inches * 2.54


def centimeters_to_inches(centimeters):
    return centimeters * 0.393701


def miles_to_kilometers(miles):
    return miles * 1, 60934


def kilometers_to_miles(kilometers):
    return kilometers * 0, 621371


def pounds_to_kilograms(pounds):
    return pounds * 0.453592


def kilograms_to_pounds(kilograms):
    return kilograms * 2.20462


def ounces_to_grams(ounces):
    return ounces * 28.3495


def grams_to_ounces(grams):
    return grams * 0.035274


def gallons_to_liters(gallons):
    return gallons * 3.78541


def liters_to_gallons(liters):
    return liters * 0.264172


def pints_to_liters(pints):
    return pints * 0.473176


def liters_to_pints(liters):
    return liters * 2.11338


def show_note():
    note = ["Для выбора конвертера введичисло",
            "1. Дюймы в сантиметры",
            "2. Сантиметры в дюймы",
            "3. Мили в километры",
            "4. Километры в мили",
            "5. Фунты в килограммы"
            "6. Килограммы в фунты",
            "7. Унции в граммы",
            "8. Граммы в унции",
            "9. Галлон в литры",
            "10. Литры в галлоны",
            "11. Пинты в литры",
            "12. Литры в пинты",
            "0. выход"]
    for string in note:
        print(string)


def converter():
    converter_number = input("Смелее: ")
    if int(converter_number) == 0:
        print("До свидания")
        return
    value = input("Значение пожалуйста: ")
    converters = [inches_to_centimeters,
                  centimeters_to_inches,
                  miles_to_kilometers,
                  kilometers_to_miles,
                  pounds_to_kilograms,
                  kilograms_to_pounds,
                  ounces_to_grams,
                  grams_to_ounces,
                  gallons_to_liters,
                  liters_to_gallons,
                  pints_to_liters,
                  liters_to_pints]

    if int(converter_number) != 0:
        print(converters[int(converter_number) - 1](int(value)))
        print("хочешь продолжить?")
        converter()


show_note()
converter()
