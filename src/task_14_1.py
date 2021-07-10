import argparse
import datetime
import time

"""Функция  дл отображение оставего времени в терминале"""


def print_timer(second):
    hours = second / 60 / 60
    minuts = (hours - int(hours)) * 60
    seconds = second - int(minuts) * 60 - int(hours) * 60 * 60
    if int(hours) == 0 and int(minuts) == 0 and seconds == 0:
        print("ALARM!!!")
    else:
        print(f"{int(hours)}:{int(minuts)}:{seconds}")


"""Вызываем текущее врямя для записи запуска скрипта в лог файл"""
time_now = datetime.datetime.now()

"""Вызываем обект argpsrse и задаемм аргументы при запуске скипта"""
parser = argparse.ArgumentParser()
parser.add_argument("-n", "--name")
parser.add_argument("-fn", "--first_name")
parser.add_argument("-ln", "--last_name")
parser.add_argument("-hr", "--hours", type=int)
parser.add_argument("-m", "--minuts", type=int)
parser.add_argument("-sc", "--seconds", type=int)
arg = parser.parse_args()

"""Записываем в лог кто и когда запускал скрипт"""
with open("log_task.txt", "a+") as file:
    append = file.write(f"{time_now} {arg.name} {arg.first_name} {arg.last_name}\n")

second = arg.hours * 60 * 60 + arg.minuts * 60 + arg.seconds

while True:

    print_timer(second)
    if second == 0:
        break
    second -= 1
    time.sleep(1)
