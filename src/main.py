# Написать программу таймер. Программа при запуске принимает имя,
# фамилию, часы, минуты и секунды. После программа начинает обратный
# отсчет выводя оставшееся время. Программа должна хранить файл
# логирования с информацией о том кто запускал программу и когда.
# Пример:
# 00:00:03
# 00:00:02
# 00:00:01
# ALARM!!!

from classes import Timer
from classes import User
from ui import TimerUI

timer1 = TimerUI()

user1 = User(timer1.name_back_input())
user1.log_user()

timer1 = Timer(*timer1.time_back_input())
timer1.timer()
