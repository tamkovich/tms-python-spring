import datetime
import sqlite3
from time import sleep


class Timer:
    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def time_to_abs_seconds(self):
        return self.hours * 60 * 60 + self.minutes * 60 + self.seconds

    @staticmethod
    def seconds_to_time(abs_seconds):
        time_seconds = abs_seconds % 60
        time_minutes = abs_seconds // 60 % 60
        time_hours = abs_seconds // 3600
        return f"{time_hours}:{time_minutes}:{time_seconds}"

    def timer(self):
        abs_sec = self.time_to_abs_seconds()
        print(abs_sec)
        for i in range(abs_sec, -1, -1):
            print(self.seconds_to_time(i))
            sleep(1)


class User:
    def __init__(self, name):
        self.name = name
        self.now = str(datetime.datetime.now())

    def log_user(self):
        # f = open("log", "a")
        # f.write(self.name + " " + self.now + "\n")
        # f.close()
        connection = sqlite3.connect("log.db")
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS tab_users_log (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                                    col_name TEXT,
                                                                    col_time_date TEXT)''')
        cursor.execute('''INSERT INTO tab_users_log(col_name, col_time_date) VALUES (?, ?)''',
                       (self.name, self.now))
        connection.commit()

# user1 = User("Вася")
# user1.log_user()

# timer1 = Timer(5, 10, 15)
# timer1.timer()

# connection = sqlite3.connect("log.db")
# cursor = connection.cursor()
# cursor.execute('''SELECT * FROM tab_users_log''',)
# table_all1 = cursor.fetchall()
# print(table_all1)
