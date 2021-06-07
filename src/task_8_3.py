def fact(number):  # функция факториала
    prz = 1
    for value in range(1, number):
        prz *= value
    return prz


def Sin1(
    x: float, n: float
) -> float:  # Задаем тип параметров вещественные и возврат фунции вещественый
    # создаем слогаемые n > 0
    list_slogaemie = [
        (-1) ** value * x ** (2 * value + 1) / fact(2 * value + 1)
        for value in range(int(n))
        if value > 0
    ]
    # формируемм список слогаемых больше n
    sum_ = sum([value for value in list_slogaemie if value > n])
    # возвращаем приблизитеьное значение sin(x)
    return (x - x ** (3 / fact(3)) + x ** (5 / fact(5))) - sum_


print(Sin1(10, 11))
