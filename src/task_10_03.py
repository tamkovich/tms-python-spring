"""Дан файл, содержащий различные даты. Каждая дата - это число, месяц и
год. Найти самую раннюю дату"""
import csv
from datetime import datetime
min_date = datetime.now()


filename = 'file_for_task_10_03.csv'
try:
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)
        for row in csvreader:
            date_ = datetime(int(row[2]), int(row[1]), int(row[0]))
            if min_date > date_:
                min_date = date_
except IndexError:
    print(f"Самая ранняя дата - {min_date}")
