class Flower:
    def __init__(self, name, height, color):
        self.__name = name
        self.__height = height
        self.__color = color

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def height(self):
        return self.__name

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    def get_description(self):
        return f"{self.__name} {self.__height}  {self.__color}"

    def get_height_category(self):
        if self.__height < 0.5:
            return "undersized"
        elif self.__height < 1:
            return "average"
        else:
            return "tall"