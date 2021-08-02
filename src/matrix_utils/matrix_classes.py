from random import randint


class Matrix:
    def __init__(self, a: int, b: int, n: int = 5, m: int = 5) -> None:
        self.n = n
        self.m = m
        self.a = a
        self.b = b
        self._data: list[list] = []

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    def gen_default_matrix(self) -> None:
        """Сгенерировать матрицу по умолчанию (нулевую)"""
        self._data = [[0 for _ in range(self.n)] for _ in range(self.m)]

    def gen_random_matrix(self) -> list:
        """Сгенерировать матрицу из случайных чисел диапозона от a до b"""
        return [[randint(self.a, self.b) for _ in range(self.m)] for _ in range(self.n)]

    def __str__(self) -> None:
        """Переопределение __str__ на построчный вывод с шапкой"""
        print(f"Матрица {self.n} на {self.m} из случайных чисел диапозона от {self.a} до {self.b}:")
        for i in self._data:
            print(i)
