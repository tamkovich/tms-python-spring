import argparse


class TimerUI:
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--name', required=True)
        parser.add_argument('--hours', required=True)
        parser.add_argument('--minutes', required=True)
        parser.add_argument('--seconds', required=True)
        self.args = parser.parse_args()

    def name_back_input(self):
        return self.args.name

    def time_back_input(self):
        return int(self.args.hours), int(self.args.minutes), int(self.args.seconds)


# timer1 = TimerUI()
# print(timer1.name_back_input())
