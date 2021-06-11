# Создать универсальный декоратор, который меняет порядок аргументов в
# функции на противоположный.

def decorator(func):
    def replace(x, y):
        x, y = y, x
        func(x, y)
    return replace


@decorator
def divv(x: int, y: int):
    res = x / y
    print(res)


divv(2, 4)
