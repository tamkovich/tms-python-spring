"""
    Программа выполняет поиск минимальной даты
    из файла и выводит ее 
"""
import json
from datetime import datetime, date

# Входные данные для json
data = {
    "date": [
        "2021/11/11",
        "2021/1/21",
        "2021/7/30",
        "2011/9/13",
        "2011/11/11",
        "2001/12/12",
        "1996/1/15",
        "2001/5/5",
        "2005/8/3",
        "2009/7/11",
    ]
}

# Создает json и передает туда даные data
with open("data.json", "w") as json_file:
    json.dump(data, json_file)

# Открывает json и считывает с него данные
with open("data.json", "r") as json_file:
    # Переводим даныне из json в dict
    temp = json.load(json_file)
    min_date = date(2022, 1, 1)
    # Переводим в дату и ноходим самую ранюю
    for row in temp["date"]:
        if datetime.strptime(row, "%Y/%m/%d").date() <= min_date:
            min_date = datetime.strptime(row, "%Y/%m/%d").date()
    print(min_date)
