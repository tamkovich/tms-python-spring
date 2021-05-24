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

# сравнение, и перевод в строку, для конкатенации
if int(rub[-1]) == 0 or 5 <= int(rub[-1]) <= 9 or int(rub[-2]) == 1:
    result += rub + " Рублей, "
elif int(rub[-1]) == 1 or int(rub) == 1:
    result += rub + " Рубль, "
elif 2 <= int(rub[-1]) <= 4:
    result += rub + " Рубля, "

# тоже самое что и с рублями)
if int(kop[-1]) == 0 or 5 <= int(kop[-1]) <= 9 or int(kop[-2]) == 1:
    result += kop + " Копеек"
elif int(kop[-1]) == 1 or int(kop) == 1:
    result += kop + " Копейка"
elif 2 <= int(kop[-1]) <= 4:
    result += kop + " Копейки"
print(result)
