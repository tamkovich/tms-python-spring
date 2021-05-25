# Получить на ввод количество рублей и копеек и вывести в правильной форме,
# например, 3 рубля, 1 рубль 25 копеек, 3 копейки

print("Введите сумму")
rub = input("Рубли: ")
kop = input("Копейки: ")

# запрет на ввод трехзначного числа
while int(kop) >= 100:
    print("Неверное число, повторите ввод!")
    kop = input("Копейки: ")
result = ""

# объявляем переменную, равную индексу последнего числа
last = len(rub) - 1
# сравнение, и перевод в строку, для конкатенации
if int(rub[last]) == 1:
    result += rub + " Рубль, "
elif int(rub[last]) == 0 or 5 <= int(rub[last]) <= 9 or int(rub[last - 1]) == 1:
    result += rub + " Рублей, "
elif 2 <= int(rub[last]) <= 4:
    result += rub + " Рубля, "

# тоже объявляем переменную
last_1 = len(kop) - 1
# тоже самое что и с рублями)
if int(kop[last_1]) == 1:
    result += kop + " Копейка"
elif int(kop[last_1]) == 0 or 5 <= int(kop[last_1]) <= 9 or int(kop[last_1 - 1]) == 1:
    result += kop + " Копеек"
elif 2 <= int(kop[last_1]) <= 4:
    result += kop + " Копейки"
print(result)
