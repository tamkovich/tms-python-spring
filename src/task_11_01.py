""" Задание 11.1

Создать пять классов описывающие реальные объекты. Каждый класс
должен содержать минимум три приватных атрибута, конструктор, геттеры
и сеттеры для каждого атрибута, два метода."""


class Wine:
    """Class of wine instances

    Describes the wine instance based on properties:
    year - the year of harvest
    color - color of the wine
    grape_sort - sort of the grape
    is_sparkling - tag of sparkling feature
    """

    def __init__(self, year, color="Red", grape_sort="Merlot", is_sparkling=False):
        self.year = year
        self.color = color
        self.grape_sort = grape_sort
        self.is_sparkling = is_sparkling

    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, new_color: str):
        COLORS = {"Red", "White", "Rose"}
        if new_color.capitalize() in COLORS:
            self.__color = new_color.capitalize()
        else:
            self.__color = "Red"

    @property
    def grape_sort(self) -> str:
        return self.__grape_sort

    @grape_sort.setter
    def grape_sort(self, grape: str):
        self.__grape_sort = grape

    @property
    def year(self) -> int:
        return self.__year

    @year.setter
    def year(self, year: int):
        if type(year) == int and year >= 0:
            self.__year = year
        else:
            self.__year = 0

    def get_info(self) -> str:
        return f"{self.color} {'sparkling' if self.is_sparkling else 'still'} {self.grape_sort} {self.year}"


class Soil:
    """Class of soil instances

    Describes the soil instance based on properties:
    soil_name - classified soil name
    density - soil density
    hpc - coefficient of horizontal pressure
    """

    def __init__(self, soil_name: str, density: float, hpc: float):
        self.soil_name = soil_name
        self.density = density
        self.hpc = hpc

    @property
    def soil_name(self) -> str: 
        return self.__soil_name

    @soil_name.setter
    def soil_name(self, soil_name: str):
        self.__soil_name = soil_name

    @property
    def density(self) -> float:
        return self.__density

    @density.setter
    def density(self, density: float):
        self.__density = density

    @property
    def hpc(self) -> float:
        return self.__hpc

    @hpc.setter
    def hpc(self, hpc: float):
        self.__hpc = hpc

    def pressure_on_depth(self, depth) -> (float, float):
        """
        Calculate a pressure on depth

        :param depth: depth (related to free surface) where the pressures calculates;
        :return: tuple of float values (vertical_pressure, horizontal_pressure)
        """
        vertical_pressure = depth * self.density
        horizontal_pressure = depth * self.density * self.hpc
        return vertical_pressure, horizontal_pressure


class Product:
    """Class of product instances

    Describes the product instance based on properties:
    firm - name of manufacturer
    name - name of product (e.g. "Milk")
    price - price of product
    """

    def __init__(self, firm: str, name: str, price: float):
        self.firm = firm
        self.name = name
        self.price = price

    @property
    def firm(self) -> str:
        return self.__firm

    @firm.setter
    def firm(self, firm: str):
        self.__firm = firm

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, price: float):
        self.__price = price

    def get_info(self) -> str:
        return f"{self.name} {self.firm} - {self.price}"


class Vehicle:
    """Class of vehicle instances

    Describes the car instance based on properties:
    firm - name of manufacturer
    model - name of vehicle model
    year - year of issue
    """
    def __init__(self, firm: str, model: str, year: int):
        self.firm = firm
        self.model = model
        self.year = year
        
    @property
    def firm(self) -> str:
        return self.__firm

    @firm.setter
    def firm(self, firm: str):
        self.__firm = firm

    @property
    def model(self) -> str:
        return self.__model

    @model.setter
    def model(self, model: str):
        self.__model = model

    @property
    def year(self) -> float:
        return self.__year

    @year.setter
    def year(self, year: float):
        self.__year = year

    def get_info(self) -> str:
        return f"{self.firm} {self.model}, {self.year} y."
        
    
class House:
    def __init__(self, floors: int, flats: int, place: str):
        self.floors = floors
        self.flats = flats
        self.place = place
    
    @property
    def floors(self) -> int:
        return self.__floors

    @floors.setter
    def floors(self, floors: int):
        self.__floors = floors
        
    @property
    def flats(self) -> int:
        return self.__flats

    @flats.setter
    def flats(self, flats: int):
        self.__flats = flats
        
    @property
    def place(self) -> str:
        return self.__place

    @place.setter
    def place(self, place: str):
        self.__place = place

    def get_info(self) -> str:
        return f"There is {self.floors}-floor house with {self.flats} flats at {self.place}."


if __name__ == "__main__":
    wine = Wine(1956, "WhitE", "Risling", False)
    print("\n", wine.get_info(), sep="", end="\n----------------------------\n")

    soil = Soil("Sand", 18, 0.33)
    vp, hp = soil.pressure_on_depth(10)
    print(f"On depth on 10 m in {soil.soil_name} soil:\n"
          f"  - the vertical pressure is {round(vp, 2)} kPa\n"
          f"  - the horizontal pressure is {round(hp, 2)} kPa", end="\n----------------------------\n")

    product = Product("'PRESIDENT'", "Camamber cheese", 10.15)
    print(f"{product.get_info()} BYN", end="\n----------------------------\n")

    car = Vehicle("Buick", "'Encore'", 2021)
    print(f"{car.get_info()}", end="\n----------------------------\n")

    house = House(4, 12, "Shchuchynshchyna, Mahileu region")
    print(f"{house.get_info()}", end="\n----------------------------\n")
