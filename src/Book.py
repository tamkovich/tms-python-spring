class Book:
    def __init__(self, title, author, year_published):
        self.__title = title
        self.__author = author
        self.__year_published = year_published

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author):
        self.__author = author

    @property
    def year_published(self):
        return self.__year_published

    @year_published.setter
    def year_published(self, year_published):
        self.__year_published = year_published

    def get_description(self):
        return f"{self.__title} {self.__author} {self.__year_published}"

    def get_century(self):
        return (self.__year_published - 1) // 100 + 1
