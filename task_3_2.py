guests = int(input("Введите количество гостей: "))
if guests >= 50:
    print("Идем в ресторан!")
elif 20 <= guests < 50:
    print("Идем в кафе!")
elif guests < 20:
    print("Празднуем дома!")