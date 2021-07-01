from src.Car import Car


class BMW(Car):
    pass


b = BMW("brand", "model", 2000, 20)
print(b.year)