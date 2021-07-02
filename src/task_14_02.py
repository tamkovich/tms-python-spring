"""Задание 14.2.

Создать программу Pomodoro.
На вход программа получает имя, фамилию, время для
фокусировки(по-умолчанию 25 минут), длину перерыва(по-умолчанию 5 минут),
количество циклов(по-умолчанию 4) и название задачи. Программа указывает
оставшееся время фокусировки, после сигнализирует о наступлении перерыва,
после сигнализирует о начале нового цикла фокусировки. Программа должна
вести файл лога о всех запусках."""

import argparse
from datetime import datetime
from os import getlogin
from time import sleep


def timer_tick(minutes: int) -> str:
    interval = minutes
    while interval >= 0:
        yield f"{interval:02d} min left"
        interval -= 1


was_started = datetime.now().strftime("%Y-%b-%d %X")

parser = argparse.ArgumentParser()
parser.add_argument('-fn', help="user firstname")
parser.add_argument('-ln', help="user lastname")
parser.add_argument('-ft', type=int, default=25, help="focus time, minutes")
parser.add_argument('-bt', type=int, default=5, help="break time, minutes")
parser.add_argument('-nc', type=int, default=4, help="number of cycles")
parser.add_argument('task', nargs="*", help="task description")
args = parser.parse_args()

if args.fn or args.ln:
    username = f"{args.fn} {args.ln}"
else:
    username = getlogin()  # If no usernames in parameters, fix current user system login

log_str = f"{was_started} {username} started pomodoro with task '{' '.join(args.task)}'. "\
          f"Focus time {args.ft} min. Break time {args.bt} min. Cycles {args.nc}.\n"

with open("log.dat", "a") as f_out:
    f_out.write(log_str)

print(log_str)

for cycle in range(args.nc):
    print(f"Cycle {cycle + 1:02d}")

    focus_timer = timer_tick(args.ft)
    print(f" Working on the task '{' '.join(args.task)}'")
    for tick in focus_timer:
        print(f"  {tick}")
        sleep(0.1)

    break_timer = timer_tick(args.bt)
    print(" Having a break")
    for tick in break_timer:
        print(f"  {tick}")
        sleep(0.1)

print("Pomodoro finished!")
