def in_to_cm(n):  # Inches to cm
    return n * 2.54, "in", "cm"  # returns (converted, source units, result units)


def cm_to_in(n):
    return n / 2.54, "cm", "in"


def mi_to_km(n):  # Miles to km
    return n * 1.609, "mi", "km"


def km_to_mi(n):
    return n / 1.609, "km", "mi"


def lb_to_kg(n):  # Pounds to kg
    return n * 0.454, "lb", "kg"


def kg_to_lb(n):
    return n / 1.609, "kg", "lb"


def oz_to_gm(n):  # Ounce to gram
    return n * 28.35, "oz", "gm"


def gm_to_oz(n):
    return n / 28.35, "gm", "oz"


def gal_to_l(n):  # Gallon to litres
    return n * 3.785, "gal", "L"


def l_to_gal(n):
    return n / 3.785, "L", "gal"


def pt_to_l(n):  # Pints to litres
    return n / 2.113, "pt", "L"


def l_to_pt(n):
    return n * 2.113, "L", "pt"


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
