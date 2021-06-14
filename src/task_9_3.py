"""
Дан файл, содержащий различные даты. Каждая дата - это число, месяц и
год. Найти самую раннюю дату. [02-8.1-ML-29]
"""
import csv
from datetime import datetime
count = 0
data = []
with open("file_data.csv", "r") as csvfile:
    csvread = csv.reader(csvfile)
    for row in csvread:
        if count != 0:
            data.append(datetime(int(row[2]), int(row[1]), int(row[0])))
        count += 1
    print(data)
    print(min(data))
