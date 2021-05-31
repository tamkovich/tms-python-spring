from datetime import date
from datetime import time
from shift import Shift

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
        time_from=time(22, 00, 00),
        time_to=time(10, 00, 00),
        date_from=date(2020, 9, 1),
        date_to=date(2020, 9, 30),
        week_days=[2, 4],
    ),
    dict(
        time_from=time(8, 00, 00),
        time_to=time(17, 00, 00),
        date_from=date(2020, 9, 1),
        date_to=date(2020, 9, 30),
        week_days=[1, 3],
    ),
    dict(
        time_from=time(22, 00, 00),
        time_to=time(11, 00, 00),
        date_from=date(2020, 1, 1),
        date_to=date(2020, 1, 10),
        week_days=[3, 4, 5],
    ),
    dict(
        time_from=time(10, 00, 00),
        time_to=time(20, 00, 00),
        date_from=date(2020, 1, 11),
        date_to=date(2020, 1, 20),
        week_days=[6, 7, 1],
    ),
]

# Пример 1 False
shift_01 = Shift(tests_false[0])
shift_02 = Shift(tests_false[1])

print(shift_01.is_intersect(shift_02))
print(shift_02.is_intersect(shift_01))

# Пример 2 True
shift_03 = Shift(tests_true[0])
shift_04 = Shift(tests_true[1])

print(shift_03.is_intersect(shift_04))
print(shift_04.is_intersect(shift_03))

shift_03 = Shift(tests_true[2])
shift_04 = Shift(tests_true[3])

print(shift_03.is_intersect(shift_04))
print(shift_04.is_intersect(shift_03))


