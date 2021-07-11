import argparse
import datetime
import time

"""Функция  для отображение оставего времени в терминале"""


def print_timer(second):
    s1 = second
    while True:   
        hours = s1 / 60 / 60
        minuts = (hours - int(hours)) * 60
        seconds = s1 - int(minuts) * 60 - int(hours) * 60 * 60
        if int(hours) == 0 and int(minuts) == 0 and seconds == 0:
            print("BREAK!!!")
            break
        else:
            print(f"{int(hours)}:{int(minuts)}:{seconds}")
            s1 -= 1
            time.sleep(0.98)

"""Вызываем текущее врямя для записи запуска скрипта в лог файл"""
time_now = datetime.datetime.now()

"""Вызываем обект argpsrse и задаемм аргументы при запуске скипта"""
parser = argparse.ArgumentParser()
parser.add_argument("-ln", "--last_name")
parser.add_argument("-mf", "--minuts_focus", default= 25,  type=int)
parser.add_argument("-mb", "--minuts_brk", default= 5,  type=int)
parser.add_argument("-ct", "--count", default= 4,  type=int)
parser.add_argument("-nt", "--name_task")
arg = parser.parse_args()

"""Записываем в лог кто и когда запускал скрипт и имя задачи"""
with open("log_task.txt", "a+") as file:
    append = file.write(f"{time_now} {arg.last_name} {arg.name_task}\n")

count = arg.count
while True:
    if count == 1:
        print_timer(arg.minuts_focus * 60)
       
    elif count != 0 :
        print_timer(arg.minuts_focus * 60)
        print_timer(arg.minuts_brk * 60)
    else:
        print("Конец работы")
        break
    count -= 1
