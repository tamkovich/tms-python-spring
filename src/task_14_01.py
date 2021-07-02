"""Задача 14.1.

Написать программу таймер. Программа при запуске принимает имя,
фамилию, часы, минуты и секунды. После программа начинает обратный
отсчет выводя оставшееся время. Программа должна хранить файл
логирования с информацией о том кто запускал программу и когда.
Пример:
00:00:03
00:00:02
00:00:01
ALARM!!!"""

import argparse
from datetime import datetime
from os import getlogin
from time import sleep


def time_str(seconds: int) -> str:  # Convert seconds into time string hh:mm:ss
    h = seconds // 3_600
    m = (seconds % 3_600) // 60
    s = ((seconds % 3_600) % 60) % 60
    return f"{h:02d}:{m:02d}:{s:02d}"


def run_timer(hours: int, minutes: int, seconds: int) -> None:
    interval = hours * 3_600 + minutes * 60 + seconds
    while interval >= 0:
        print(time_str(interval))
        sleep(0.1)
        interval -= 1


was_started = datetime.now().strftime("%Y-%b-%d %X")

parser = argparse.ArgumentParser()
parser.add_argument('-fn', help="user firstname")
parser.add_argument('-ln', help="user lastname")
parser.add_argument('-hr', type=int, choices=list(range(24)), default=0, help="hours")
parser.add_argument('-m', type=int, choices=list(range(60)), default=0, help="minutes")
parser.add_argument('-s', type=int, choices=list(range(60)), default=0, help="seconds")
args = parser.parse_args()

if args.fn or args.ln:
    username = f"{args.fn} {args.ln}\n"
else:
    username = f"{getlogin()}\n"  # If no usernames in parameters, fix current user system login

log_str = f"{was_started} {username}"

with open("log.dat", "a") as f_out:
    f_out.write(log_str)

run_timer(args.hr, args.m, args.s)
print("ALARM!!!")
