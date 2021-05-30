from datetime import date
from shift import Shift
from datetime import time

tests_false = [
    dict(
        time_from=time(8, 0, 00),
        time_to=time(17, 00, 00),
        date_from=date(2020, 1, 1),
        date_to=date(2020, 1, 10),
        week_days=[1, 2, 3],
    ),
    dict(
        time_from=time(17, 00, 00),
        time_to=time(4, 00, 00),
        date_from=date(2020, 1, 1),
        date_to=date(2020, 1, 10),
        week_days=[1, 2, 3],
    ),
]

tests_true = [
    dict(
        time_from=time(8, 0, 00),
        time_to=time(5, 00, 00),
        date_from=date(2020, 1, 1),
        date_to=date(2020, 1, 10),
        week_days=[1, 2, 3],
    ),
    dict(
        time_from=time(10, 00, 00),
        time_to=time(13, 00, 00),
        date_from=date(2020, 1, 1),
        date_to=date(2020, 1, 10),
        week_days=[1, 2, 3],
    ),
]

# Пример 1 True
shift_01 = Shift(tests_false[0])
shift_02 = Shift(tests_false[1])

print(shift_01.is_intersect(shift_02))
print(shift_02.is_intersect(shift_01))


# Пример 2 False
shift_03 = Shift(tests_true[0])
shift_04 = Shift(tests_true[1])

print(shift_03.is_intersect(shift_04))
print(shift_04.is_intersect(shift_03))



