import argparse
from generator import gen
from logging import log
import time

parser = argparse.ArgumentParser()
parser.add_argument('-fn', '--first-name', required=True)
parser.add_argument('-ln', '--last-name', required=True)
parser.add_argument('-hn', '--hour', required=False)
parser.add_argument('-mn', '--minute', required=False)
parser.add_argument('-sn', '--second', required=False)
args = parser.parse_args()

input_date = (args.hour + ':' + args.minute + ':' + args.second)

gen = gen(input_date)
while True:
    try:
        print(next(gen))
        time.sleep(1)
    except StopIteration:
        break

print("ALARM!!")

log(args, 'logs.txt')
