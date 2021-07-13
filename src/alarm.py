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


parser = argparse.ArgumentParser()
parser.add_argument('-fn', '--first-name', required=True)
parser.add_argument('-ln', '--last-name', required=True)
parser.add_argument('-hh', '--hour', type=int)
parser.add_argument('-mm', '--minute', type=int)
parser.add_argument('-ss', '--second', type=int)
args = parser.parse_args()
time1 = datetime.datetime.now()

with open('result.txt', 'w') as f:
    f.write(str(time1) + '\n')
    f.write(args.first_name + '\n')
    f.write(args.last_name + '\n')
    f.write(f'hours {str(args.hour)} minutes {str(args.minute)} seconds {str(args.second)}')


def time_in_seconds(time: datetime):
    return time.hour * 3600 + time.minute * 60 + time.second


def time_to_time(second):
    hour = second // 3600
    minute = (second % 3600) // 60
    second = (second % 60) % 60
    return datetime.time(hour, minute, second)


your_time = time_in_seconds(datetime.time(int(args.hour), int(args.minute), int(args.second)))
while your_time >= 0:
    print(time_to_time(your_time))
    sleep(1)
    your_time -= 1
print('Alarm!!!')
