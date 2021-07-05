import sys, time
from playsound import playsound

def log(file, info_to_log):
    with open(file, 'a') as f:
        f.write(f'{info_to_log}\n')

def user_input():
    interval = int(input('Please Enter duration (mins) of interval: '))
    break_duration = int(input('Please Enter break duration(mins) of interval: '))
    total_duration = int(input('Please enter number of sessions: '))
    task = input('Please enter a task name: ')
    return interval, break_duration, total_duration, task


def countdown(interval):
    for i in range(interval-1, -1, -1):
        for j in range(59, -1, -1):
            sys.stdout.write(f'\rDuration: \
            {i} : {j} left')
            log('log.txt', f'{i} : {j} left')
            time.sleep(1)
            sys.stdout.flush()

if __name__ == "__main__":
    session_count = 0
    interval, break_duration, total_duration, task = user_input()
    log('log.txt', f'duration (mins) of interval: {interval}')
    log('log.txt', f'break duration (mins) of interval: {break_duration}')
    log('log.txt', f'number of sessions: {total_duration}')
    log('log.txt', f'task: {task}')

    while session_count < total_duration:
        playsound(r'c:\windows\media\alarm02.wav')
        countdown(interval)
        playsound(r'c:\windows\media\alarm02.wav')
        print('\nBreak time!')
        countdown(break_duration)
        session_count += 1
        print('\nsession number: ', session_count)
    print('\nEnd of Session!')
