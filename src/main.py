from datetime import time
from datetime import date
from shift import Shift

# Пример 1
shift_01 = Shift(time(8, 0, 0), time(17, 0, 0), date(2020, 1, 1), date(2020, 1, 10), [1, 2, 3])
shift_02 = Shift(time(17, 0, 0), time(4, 0, 0), date(2020, 1, 1), date(2020, 1, 10), [1, 2, 3])

print(shift_01.is_intersect(shift_02))
print(shift_02.is_intersect(shift_01))


# Пример 2
shift_03 = Shift(time(8, 0, 0), time(5, 0, 0), date(2020, 1, 1), date(2020, 1, 10), [1, 2, 3])
shift_04 = Shift(time(10, 0, 0), time(13, 0, 0), date(2020, 1, 1), date(2020, 1, 10), [1, 2, 3])

print(shift_03.is_intersect(shift_04))
print(shift_04.is_intersect(shift_03))



