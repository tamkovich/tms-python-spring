"""
Homework - 10
task_10_3: Дан файл, содержащий различные даты. Каждая дата - это число, месяц и
год. Найти самую раннюю дату. [02-8.1-ML-29]
"""

import csv
from csv_utils import write_csv
from datetime import datetime

write_csv([["01.01.21"],
           ["09.03.11"],
           ["10.05.15"],
           ["10.07.07"],
           ["11.03.03"],
           ["05.11.16"],
           ["12.12.14"],
           ["30.08.20"],
           ["01.01.01"],
           ["13.07.10"],
           ["14.02.12"],
           ["25.03.17"],
           ["15.01.19"],
           ["19.11.11"],
           ["16.07.06"],
           ["16.07.19"],
           ["17.07.14"],
           ["17.07.09"],
           ["18.07.11"],
           ["18.07.16"],
           ["19.07.07"],
           ["19.07.17"]
           ],
          "date_file.csv")

with open("date_file.csv", "r") as fd:
    list_dates_str = ["".join(date) for date in csv.reader(fd)]
    print(list_dates_str)
    list_dates = [datetime.strptime(date, "%d.%m.%y") for date in list_dates_str]
    print(max(list_dates))
    print(min(list_dates))
