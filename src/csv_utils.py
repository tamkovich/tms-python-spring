# Функции по работе с csv файлами:
# Задание 10.08  (HW)

# Чтение.


def reading_csv(file_read: str) -> list:
    """Открывает файл для чтения, формирует и возвращает список строк"""
    import csv
    with open(file_read, "r") as f:
        finish_list_read = [row for row in csv.reader(f)]
    return finish_list_read


if __name__ == "__main__":
    print(reading_csv("file1.csv"))


# Запись (перезапись).


def write_csv(input_list: list, file_name_write: str) -> None:
    """Создает/открывает файл для записи и записывает в него входящий список по строкам"""
    import csv
    with open(file_name_write, "w") as f2:
        csv_writer = csv.writer(f2, lineterminator="\n")
        csv_writer.writerows(input_list)


if __name__ == "__main__":
    write_csv([["картина", "корзина", "собаченка"], [1, 2, 3, 4, 5]], "file11.csv")


# Добавление записи (по позиции, по-умолчанию в конец).


def write_pos_csv(input_list_pos: list, file_name_write_pos: str, position=-1) -> None:
    """Читает файл в список, добавляет позицию и перезаписывает новый список в тот же файл"""
    import csv
    with open(file_name_write_pos, "r") as f3:
        list_write_pos = [row1 for row1 in csv.reader(f3)]
    if position == -1:
        list_write_pos.append(input_list_pos)
    else:
        list_write_pos.insert(position, input_list_pos)
    with open(file_name_write_pos, "w") as f4:
        csv_writer = csv.writer(f4, lineterminator="\n")
        csv_writer.writerows(list_write_pos)


if __name__ == "__main__":
    write_pos_csv(["тест", "записи", "без", "позиции"], "file11.csv")


# Удаление записи(по позиции,по-умолчанию последнюю).


def del_pos_csv(file_name_del_pos: str, position=-1) -> None:
    """Читает файл в список, удаляет позицию и перезаписывает новый список в тот же файл"""
    import csv
    with open(file_name_del_pos, "r") as f5:
        list_del_pos = [row2 for row2 in csv.reader(f5)]
    del list_del_pos[position]
    with open(file_name_del_pos, "w") as f6:
        csv_writer = csv.writer(f6, lineterminator="\n")
        csv_writer.writerows(list_del_pos)


if __name__ == "__main__":
    del_pos_csv("file11.csv", 1)


# Задание 10.09  (HW)
# 1) Функция подсчета полной стоимости всех товаров.


def full_cost_csv(file_name_full_cost: str) -> int:
    """В 0 стр. находит индексы цены и количества, по ним считает стоимость в остальных строках"""
    import csv
    full_cost = 0
    with open(file_name_full_cost, "r") as f6:
        temp_list_header = list(csv.reader(f6))[0]
        for i, elem in enumerate(temp_list_header):
            if elem == "Цена":
                index_price = i
            elif elem == "Количество":
                index_quantity = i
    with open(file_name_full_cost, "r") as f7:
        temp_list_product = list(csv.reader(f7))[1:]
        for i1 in temp_list_product:
            cost_product = int(i1[index_price]) * int(i1[index_quantity])
            full_cost += cost_product
    return full_cost


if __name__ == "__main__":
    print(f'Полная стоимость всех товаров = {full_cost_csv("product_inf.csv")}')


# 2) Функция поиска самого дорогого товара.


def max_price_csv(file_name_max_price: str) -> list:
    """В 0 стр. находит индекс цены, находит max цену в остальных стр. и отбирает товары по ней"""
    import csv
    product_max_price = []
    with open(file_name_max_price, "r") as f8:
        for j, elem in enumerate(list(csv.reader(f8))[0]):
            if elem == "Цена":
                index_max_price = j
    with open(file_name_max_price, "r") as f9:
        max_price = max([int(j1[index_max_price]) for j1 in list(csv.reader(f9))[1:]])
    with open(file_name_max_price, "r") as f10:
        for j2 in list(csv.reader(f10))[1:]:
            if int(j2[index_max_price]) == max_price:
                product_max_price.append(j2)
    return product_max_price


if __name__ == "__main__":
    print(f'Самый дорогой товар = {max_price_csv("product_inf.csv")}')


# 3) Функция поиска самого дешевого товара.


def min_price_csv(file_name_min_price: str) -> list:
    """В 0 стр. находит индекс цены, находит min цену в остальных стр. и отбирает товары по ней"""
    import csv
    product_min_price = []
    with open(file_name_min_price, "r") as f11:
        for k, elem in enumerate(list(csv.reader(f11))[0]):
            if elem == "Цена":
                index_min_price = k
    with open(file_name_min_price, "r") as f12:
        min_price = min([int(k1[index_min_price]) for k1 in list(csv.reader(f12))[1:]])
    with open(file_name_min_price, "r") as f13:
        for k2 in list(csv.reader(f13))[1:]:
            if int(k2[index_min_price]) == min_price:
                product_min_price.append(k2)
    return product_min_price


if __name__ == "__main__":
    print(f'Самый дешевый товар = {min_price_csv("product_inf.csv")}')


# 4) Функция уменьшения количества товара(на n, по-умолчанию на 1)

def del_quantity_csv(file_name_del_quantity: str, product_name: str, n=1) -> None:
    """Читает файл в список, уменьшает количество нужного товара по его названию

    и индексу кол-ва из 0 стр., формирует новый список и перезаписывает его в файл
    """
    import csv
    with open(file_name_del_quantity, "r") as f14:
        for ll, elem in enumerate(list(csv.reader(f14))[0]):
            if elem == "Количество":
                index_del_quantity = ll
    with open(file_name_del_quantity, "r") as f15:
        list_del_quantity = [row3 for row3 in csv.reader(f15)]
    for m in list_del_quantity:
        if m[0] == product_name:
            m[index_del_quantity] = str(int(m[index_del_quantity]) - n)
    with open(file_name_del_quantity, "w") as f16:
        csv_writer = csv.writer(f16, lineterminator="\n")
        csv_writer.writerows(list_del_quantity)


if __name__ == "__main__":
    del_quantity_csv("product_inf.csv", "зажигалка", 10)


# task_10_1  (HW)
# Функция классификации людей по возрасту.


def age_classification_csv(file_name_age_classification: str) -> dict:
    """В 0 стр. находит индекс возраста, по нему классиф. остальные данные"""
    import csv
    with open(file_name_age_classification, "r") as f17:
        for o, elem in enumerate(list(csv.reader(f17))[0]):
            if elem == "Возраст":
                index_age = o
    with open(file_name_age_classification, "r") as f18:
        temp_list_age = list(csv.reader(f18))[1:]
        count_1_12 = 0
        count_13_18 = 0
        count_19_25 = 0
        count_26_40 = 0
        count_41_more = 0
        for p in temp_list_age:
            if 1 <= int(p[index_age]) <= 12:
                count_1_12 += 1
            elif 13 <= int(p[index_age]) <= 18:
                count_13_18 += 1
            elif 19 <= int(p[index_age]) <= 25:
                count_19_25 += 1
            elif 26 <= int(p[index_age]) <= 40:
                count_26_40 += 1
            elif int(p[index_age]) >= 41:
                count_41_more += 1
    dict_age_class = {
        "people 1-12 age": count_1_12,
        "people 13-18 age": count_13_18,
        "people 19-25 age": count_19_25,
        "people 26-40 age": count_26_40,
        "people more 40 age": count_41_more,
    }
    return dict_age_class


if __name__ == "__main__":
    print(age_classification_csv("people_inf.csv"))


# task_10_2   (HW)
# Нахождение средней погоды (скорость ветра и градусы) за последние 7 дней.


def average_weather_csv(file_name_average_weather: str, city: str, days=2) -> tuple:
    """Находит индексы всех параметров, формирует списки нужных по фильтрам и считает средние"""
    import csv
    import datetime
    with open(file_name_average_weather, "r") as f19:
        for r, elem in enumerate(list(csv.reader(f19))[0]):
            if elem == "Дата":
                index_date = r
            elif elem == "Место":
                index_city = r
            elif elem == "Градусы":
                index_temper = r
            elif elem == "Скорость ветра":
                index_wind = r
    with open(file_name_average_weather, "r") as f20:
        temp_list_weather = list(csv.reader(f20))[1:]
        temp_list_temper = []
        temp_list_wind = []
        for s in temp_list_weather:
            if s[index_city] == city and \
                    (datetime.datetime.now() - datetime.datetime.strptime(s[index_date],
                                                                          "%d.%m.%y")).days < days:
                temp_list_temper.append(float(s[index_temper]))
                temp_list_wind.append(float(s[index_wind]))
    average_temper = sum(temp_list_temper) / len(temp_list_temper)
    average_wind = sum(temp_list_wind) / len(temp_list_wind)
    return average_temper, average_wind


if __name__ == "__main__":
    temper, wind = average_weather_csv("weather_inf.csv", "Минск", 7)
    print(f'Средняя температура = {temper}, средняя скорость ветра = {wind}')
