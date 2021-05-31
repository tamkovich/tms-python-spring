from datetime import date
from datetime import time
from shift import Shift
import unittest


class TestShift(unittest.TestCase):
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

    def test_true_is_intersect(self):
        for test_case in self.true_tests:
            shift_01 = Shift(test_case[0]['time_from'], test_case[0]['time_to'],
                             test_case[0]['date_from'], test_case[0]['date_to'], test_case[0]['week_days'])
            
            shift_02 = Shift(test_case[1]['time_from'], test_case[1]['time_to'],
                             test_case[1]['date_from'], test_case[1]['date_to'], test_case[1]['week_days'])

            with self.subTest(shift_02):
                self.assertTrue(shift_01.is_intersect(shift_02))

    def test_false_is_intersect(self):
        for test_case in self.false_tests:
            shift_01 = Shift(test_case[0]['time_from'], test_case[0]['time_to'],
                             test_case[0]['date_from'], test_case[0]['date_to'], test_case[0]['week_days'])

            shift_02 = Shift(test_case[1]['time_from'], test_case[1]['time_to'],
                             test_case[1]['date_from'], test_case[1]['date_to'], test_case[1]['week_days'])

            with self.subTest(shift_02):
                self.assertFalse(shift_01.is_intersect(shift_02))


if __name__ == '__main__':
    unittest.main()
