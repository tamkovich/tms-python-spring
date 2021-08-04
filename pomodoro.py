"""
Homework - 14
task_14_02: Создать программу Pomodoro.
На вход программа получает имя, фамилию, время для
фокусировки(по-умолчанию 25 минут), длину перерыва(по-умолчанию 5 минут),
количество циклов(по-умолчанию 4) и название задачи. Программа указывает
оставшееся время фокусировки, после сигнализирует о наступлении перерыва,
после сигнализирует о начале нового цикла фокусировки. Программа должна
вести файл лога о всех запусках.
"""
import argparse
import src.func_pomodoro

parser = argparse.ArgumentParser()
parser.add_argument('-fn', '--first_name', type=str, required=True)
parser.add_argument('-ln', '--last_name', type=str, required=True)
parser.add_argument('-ft', '--focus_time', type=int, default=25, required=False)
parser.add_argument('-u_break', type=int, default=5, required=False)
parser.add_argument('-cycles', type=int, default=4, required=False)
args = parser.parse_args()

fn = args.first_name
ln = args.last_name
ft = int(args.focus_time)
br = int(args.u_break)
cyc = int(args.cycles)


if __name__ == "__main__":
    src.func_pomodoro.log_func(fn, ln, ft, br, cyc)
    pomodoro = src.func_pomodoro.step_pomodoro(ft, br, cyc)
    for i in range(cyc):
        next(pomodoro)
        next(pomodoro)
