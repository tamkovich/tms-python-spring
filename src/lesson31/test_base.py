"""
Можно ли суммировать список целых чисел?
Можно ли суммировать кортеж или множество?
Можно ли суммировать список чисел с плавающей точкой?
Что будет, если дать на вход плохое значение: одно целое число или строку?
Что будет, если одно из значений отрицательное?
"""
import pytest

from base import sum, minus


def test_sum_list_of_numbers():
    with pytest.raises(TypeError):
        sum([1, 2, 3])


@pytest.mark.parametrize(
    'first_number, second_number, expected_result',
    [
        (1, 3, 4),
        (2, 4, 6),
        (0, 0, 0),
    ],
)
def test_sum_works_with_1_and_2(first_number, second_number, expected_result):
    assert sum(first_number, second_number) == expected_result


def test_sum_works_with_1_and_3():
    assert sum(1, 3) == 4
