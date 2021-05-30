# Задание 5.2
# Дано число. Найти сумму и произведение его цифр.

need_works = True

while need_works:
    number = input("Enter your number (x - exit): ")

    if number.isdigit():
        summ, product = 0, 1
        number = int(number)

        while number >= 10:
            summ += number % 10
            product *= number % 10
            number //= 10
        summ += number
        product *= number
        print(f"Sum of number's digits: {summ}.\nProduct of number's digits: {product}\n")

    elif number == "x":
        need_works = False

    else:
        print("You've entered not a number. Try again.\n")
