"""
 Нахождения сумма и максималного элемента
"""


def fun_sum_max(*args):
    return sum(args), max(args)


summa, max_ = fun_sum_max(2, 5, -3, 8, 5)
print(f"Сумма элементов: {summa}, Максимальный элемент: {max_}")
