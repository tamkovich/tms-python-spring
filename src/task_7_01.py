# Задание 7.1.
# Написать 12 функций по переводу:
# 1. Дюймы в сантиметры
# 2. Сантиметры в дюймы
# 3. Мили в километры
# 4. Километры в мили
# 5. Фунты в килограммы
# 6. Килограммы в фунты
# 7. Унции в граммы
# 8. Граммы в унции
# 9. Галлон в литры
# 10. Литры в галлоны
# 11. Пинты в литры
# 12. Литры в пинты
# Примечание: функция принимает на вход число и возвращает конвертированное число
# 2. Написать программу, со следующим интерфейсом: пользователю предоставляется на
# выбор 12 вариантов перевода(описанных в первой задаче). Пользователь вводит цифру
# от одного до двенадцати. После программа запрашивает ввести численное значение.
# Затем программа выдает конвертированный результат. Использовать функции из первого
# задания. Программа должна быть в бесконечном цикле. Код выхода из программы - “0”.


def in_to_cm(inches):  # Inches to cm
    return inches * 2.54, "in", "cm"  # returns (converted, source units, result units)


def cm_to_in(centimeters):
    return centimeters / 2.54, "cm", "in"


def mi_to_km(miles):  # Miles to km
    return miles * 1.609, "mi", "km"


def km_to_mi(kilometers):
    return kilometers / 1.609, "km", "mi"


def lb_to_kg(pounds):  # Pounds to kg
    return pounds * 0.454, "lb", "kg"


def kg_to_lb(kilograms):
    return kilograms / 1.609, "kg", "lb"


def oz_to_gm(ounces):  # Ounce to gram
    return ounces * 28.35, "oz", "gm"


def gm_to_oz(grams):
    return grams / 28.35, "gm", "oz"


def gal_to_l(gallons):  # Gallon to litres
    return gallons * 3.785, "gal", "L"


def l_to_gal(litres):
    return litres / 3.785, "L", "gal"


def pt_to_l(pints):  # Pints to litres
    return pints / 2.113, "pt", "L"


def l_to_pt(litres):
    return litres * 2.113, "L", "pt"


def show_menu(menu):
    for elem in menu:
        print(elem)
    print("----------------------")


def get_user_choice():
    CHOICE = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"}
    while True:
        choice = input("Your choice: ")
        if choice in CHOICE:
            return int(choice)
        else:
            print("Incorrect choice. Try again, please.\n")


def get_value():
    while True:
        value = input("Enter the value to convert: ")
        value = value.replace(",", ".")
        if value.replace(".", "", 1).isdigit():
            return float(value)
        else:
            print("Incorrect value. Try again, please.")


converters = [in_to_cm, cm_to_in,
              mi_to_km, km_to_mi,
              lb_to_kg, kg_to_lb,
              oz_to_gm, gm_to_oz,
              gal_to_l, l_to_gal,
              pt_to_l, l_to_pt]

MENU = ["1 - Inches to Centimeters",
        "2 - Centimeters to inches",
        "3 - Miles to kilometers",
        "4 - Kilometers to miles",
        "5 - Pounds to kilograms",
        "6 - Kilograms to pounds",
        "7 - Ounces to grams",
        "8 - Grams to ounces",
        "9 - Gallons to liters",
        "10 - Liters to Gallons",
        "11 - Pints to liters",
        "12 - Liters to pints",
        "0 - exit"]

while True:
    print("----------------------",
          "AVAILABLE CONVERSIONS:", sep="\n")

    show_menu(MENU)
    user_choice = get_user_choice()

    if user_choice == 0:
        break

    print(f"We are going to do conversion №{MENU[user_choice - 1]}.")

    val = get_value()
    converted_value, unit_src, unit_res = converters[user_choice - 1](val)
    print(f"{val} {unit_src} = {round(converted_value, 1)} {unit_res}")
    input("\nPress ENTER to continue.\n")

print("Exit the program.")
