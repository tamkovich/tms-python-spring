# task_8_01
# my first test recursive function
def double_recurs_factorial(n: int) -> int:
    return n if n == 1 or n == 2 else n * double_recurs_factorial(n - 2)


# task_8_02
def polindr(n: str):
    print(n) if n == n[:: -1] else n
