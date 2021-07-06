"""
Написать программу таймер. Программа при запуске принимает имя,
фамилию, часы, минуты и секунды. После программа начинает обратный
отсчет выводя оставшееся время. Программа должна хранить файл
логирования с информацией о том кто запускал программу и когда.
Пример:
00:00:03
00:00:02
00:00:01
ALARM!!!
"""
import argparse
import datetime
from time import sleep


def time_translate_toseconds(time_: datetime):
    return time_.hour * 3600 + time_.minute * 60 + time_.second


def time_translate_to_time(second_):
    hour = second_ // 3600
    minute = (second_ % 3660) // 60
    second = (second_ % 60) % 60
    return datetime.time(hour, minute, second)


time_today = datetime.datetime.now()
parser = argparse.ArgumentParser()
parser.add_argument('-fn', '--first-name', required=True)
parser.add_argument('-ln', '--last-name', required=True)
parser.add_argument('--hour', required=True)
parser.add_argument('--minute', required=True)
parser.add_argument('--second', required=True)
args = parser.parse_args()
print(args)
created_time =\
    time_translate_toseconds(datetime.time(int(args.hour), int(args.minute), int(args.second)))
while created_time >= 0:
    print(time_translate_to_time(created_time))
    sleep(1)
    created_time -= 1
print('First name:', args.first_name)
print('Last name:', args.last_name)
print(time_today)
