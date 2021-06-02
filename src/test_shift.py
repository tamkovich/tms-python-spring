# python -m pytest -v -rfEsxXpP

from datetime import date
from datetime import time
from shift import Shift
import pytest

true_tests = [
    (
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
    ),
    (
        dict(
            time_from=time(8, 00, 00),
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
    ),
    (
        dict(
            time_from=time(8, 00, 00),
            time_to=time(15, 00, 00),
            date_from=date(2020, 1, 1),
            date_to=date(2020, 1, 10),
            week_days=[1, 2, 3],
        ),
        dict(
            time_from=time(8, 00, 00),
            time_to=time(15, 00, 00),
            date_from=date(2020, 1, 1),
            date_to=date(2020, 1, 10),
            week_days=[1, 2, 3],
        ),
    ),
    (
        dict(
            time_from=time(8, 00, 00),
            time_to=time(17, 00, 00),
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
    ),
    (
        dict(
            time_from=time(8, 00, 00),
            time_to=time(17, 00, 00),
            date_from=date(2020, 1, 1),
            date_to=date(2020, 1, 10),
            week_days=[1, 2, 3],
        ),
        dict(
            time_from=time(10, 00, 00),
            time_to=time(20, 00, 00),
            date_from=date(2020, 1, 1),
            date_to=date(2020, 1, 10),
            week_days=[1, 2, 3],
        ),
    ),
    (
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
    ),
]

false_tests = [
    (
        dict(
            time_from=time(8, 00, 00),
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
    ),
    (
        dict(
            time_from=time(22, 00, 00),
            time_to=time(5, 00, 00),
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
    ),
]


@pytest.mark.parametrize("s1,s2", [(true_tests[0][0], true_tests[0][1]),
                                   (true_tests[1][0], true_tests[1][1]),
                                   (true_tests[2][0], true_tests[2][1]),
                                   (true_tests[3][0], true_tests[3][1]),
                                   (true_tests[4][0], true_tests[4][1]),
                                   (true_tests[5][0], true_tests[5][1])])
def test_true_is_intersect(s1, s2):
    shift_01 = Shift(s1['time_from'], s1['time_to'],
                     s1['date_from'], s1['date_to'],
                     s1['week_days'])

    shift_02 = Shift(s2['time_from'], s2['time_to'],
                     s2['date_from'], s2['date_to'],
                     s2['week_days'])
    assert shift_01.is_intersect(shift_02) == True


@pytest.mark.parametrize("s1,s2", [(false_tests[0][0], false_tests[0][1]),
                                   (false_tests[1][0], false_tests[1][1])])
def test_false_is_intersect(s1, s2):
    shift_01 = Shift(s1['time_from'], s1['time_to'],
                     s1['date_from'], s1['date_to'],
                     s1['week_days'])

    shift_02 = Shift(s2['time_from'], s2['time_to'],
                     s2['date_from'], s2['date_to'],
                     s2['week_days'])
    assert shift_01.is_intersect(shift_02) == False
