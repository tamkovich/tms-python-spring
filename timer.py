"""
Homework - 14
task_14_01: Написать программу таймер.
Программа при запуске принимает фамилию, имя, часы, минуты и секунды.
После программа начинает обратный отсчет выводя оставшееся время.
Программа должна хранить файл логирования с инф. о том
кто и когда запускал программу.
Пример :
00:00:03
00:00:02
00:00:01
ALARM!!!
"""
import argparse
from datetime import timedelta
import time

parser = argparse.ArgumentParser()
parser.add_argument('-fn', '--first_name', required=True)
parser.add_argument('-ln', '--last_name', required=True)
parser.add_argument('-hr', '--hours', required=True)
parser.add_argument('-m', '--minutes', required=True)
parser.add_argument('-s', '--seconds', required=True)
args = parser.parse_args()

total_seconds = int(args.hours) * 3600 + int(args.minutes) * 60 + int(args.seconds)

with open('src/log.txt', "a") as f:
    f.write(f"first name: {args.first_name} last name: {args.last_name} "
            f"timer: {str(timedelta(seconds=total_seconds))}\n")

for i in range(total_seconds, 0, -1):
    print(str(timedelta(seconds=i)))
    time.sleep(1)
print("ALARM!!!")
