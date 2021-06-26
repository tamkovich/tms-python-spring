from ui_func import *

while True:
    try:
        choice = get_user_choice()
    except OperationTypeException as error:
        print(f"\nAn error has occurred. {error}\n")
        choice = "0"

    if choice == "0":
        break
    a, b = get_operands()
    result = calculate(choice, a, b)
    print(f"{a} {choice} {b} = {result:.2f}"
          "\n-------------------------------------")

print("Exit program.")
