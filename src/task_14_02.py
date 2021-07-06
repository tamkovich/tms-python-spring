"""
Создать программу Pomodoro.
На вход программа получает имя, фамилию, время для
фокусировки(по-умолчанию 25 минут), длину перерыва(по-умолчанию 5 минут),
количество циклов(по-умолчанию 4) и название задачи. Программа указывает
оставшееся время фокусировки, после сигнализирует о наступлении перерыва,
после сигнализирует о начале нового цикла фокусировки. Программа должна
вести файл лога о всех запусках.
"""
import argparse
import datetime
from time import sleep


def remaining_time(time):
    while time > 0:
        print(time)
        sleep(1)
        time -= 1


parser = argparse.ArgumentParser()
parser.add_argument('-fn', '--first_name', required=True)
parser.add_argument('-ln', '--last_name', required=True)
parser.add_argument('--time_to_focus', required=True)
parser.add_argument('--break_length', required=True)
parser.add_argument('--number_of_cycles', required=True)
parser.add_argument('--task_names', required=True)
args = parser.parse_args()
print(args)
time_now = datetime.datetime.now().strftime("%Y-%b-%d %X")
cycles = int(args.number_of_cycles)
while cycles > 0:
    logo_list = f"{time_now}: {args.first_name} {args.last_name}" \
                f" Focus time {args.time_to_focus} Break time {args.break_length}" \
                f" Cycles {args.number_of_cycles} task names {args.task_names}\n"

    with open("logo.txt", "a") as f:
        f.write(logo_list)
    print("Время фокусировки:")
    remaining_time(int(args.time_to_focus))
    print("Время перерыва")
    remaining_time(int(args.break_length))
    cycles -= 1
