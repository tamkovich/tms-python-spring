# Homework - 03
# task_3_10:
# Получить на ввод количество руб. и коп. и вывести в правильной форме,
# например, 3 рубля, 1 рубль 25 копеек, 3 копейки
cost = input("Введите стоимость в формате руб,коп: ")
cost_list = cost.split(",")
if int(cost_list[0]) == 1:
    print(f"Стоимость: {cost_list[0]} рубль {cost_list[1]} копеек")
else:
    if 2 < int(cost_list[0]) < 5:
        print(f"Стоимость: {cost_list[0]} рубля {cost_list[1]} копеек")
    else:
        print(f"Стоимость: {cost_list[0]} рублей {cost_list[1]} копеек")
