from datetime import datetime, timedelta


def gen(date_time_str):
    date_time_obj = datetime.strptime(date_time_str, '%H:%M:%S')
    while date_time_obj.second + date_time_obj.minute + date_time_obj.hour !=0:
        yield date_time_obj.time()
        date_time_obj = date_time_obj + timedelta(days=0, hours=0, minutes=0, seconds=-1)

