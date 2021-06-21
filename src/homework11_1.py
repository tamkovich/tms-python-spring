# Создать пять классов описывающие реальные объекты. Каждый класс
# должен содержать минимум три приватных атрибута, конструктор, геттеры
# и сеттеры для каждого атрибута, два метода.

class Account:
    def __init__(self, name, password, email, color):
        self.__name = name
        self.__password = password
        self.__email = email
        self.__color = color

    # attribute getter
    @property
    def name(self):
        return self.__name

    # attribute setter
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    def show_email(self):
        print('Email address is ', self.email)

    def theme(self):
        print('Color theme is ', self.color)


vk = Account('john', 'qwerty', 'qwerty@asd.com', 'dark')
vk.email = 'new_address@mail.com'
vk.show_email()
vk.theme()


print('-------------')


class Shop:
    def __init__(self, admin, address, money):
        self.__admin = admin
        self.__address = address
        self.__money = int(money)

    # attribute getter
    @property
    def admin(self):
        return self.__admin

    # attribute setter
    @admin.setter
    def admin(self, admin):
        self.__admin = admin

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        self.__address = address

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, money):
        self.__money = money

    def take_money(self):
        if self.money < 100:
            self.money = 0
            print('Cashbox money - ', self.money)
        else:
            print('Limit is one franklin banknote!')

    def holiday(self):
        self.money -= 50
        print('Great holyday!')
        print('Balance ', self.money)


sklep = Shop('Greg', 'Akapulka', 120)
sklep.holiday()
sklep.take_money()
print('-------------')


class Game:
    def __init__(self, name, price, author):
        self.__name = name
        self.__author = author
        self.__price = int(price)

    # attribute getter
    @property
    def name(self):
        return self.__name

    # attribute setter
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author):
        self.__author = author

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

    def discount(self, discount=10):
        return self.price * (100-discount)

    def info(self):
        print(f'Game {self.name} in price for {self.price}, author {self.author}.')


ch = Game('chess', 1, 'persia')
ch.info()
print('-------------')


class Table:
    def __init__(self, size, color, owner, age):
        self.__size = size
        self.__color = color
        self.__owner = owner
        self.__age = age

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        self.__size = size

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, owner):
        self.__owner = owner

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    def holiday(self):
        print(f'Table {self.color} color was decorated in honor of {self.owner}.')

    def reincarnation(self):
        self.age = 0
        print('new age is ', self.age)


class Exam:
    def __init__(self, subject, professor, level, stress):
        self.__subject = subject
        self.__professor = professor
        self.__level = level
        self.__stress = stress

    @property
    def subject(self):
        return self.__subject

    @subject.setter
    def subject(self, subject):
        self.__subject = subject

    @property
    def professor(self):
        return self.__professor

    @professor.setter
    def professor(self, professor):
        self.__professor = professor

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, level):
        self.__level = level

    @property
    def stress(self):
        return self.__stress

    @stress.setter
    def stress(self, stress):
        self.__stress = stress

    def gift(self):
        print(f'You give gift to {self.professor} and reduced your stress to 20 points {self.stress-20}.')

    def drugs(self):
        self.stress = 0
        print('You lost 20$ and set your stress level to 0.')


f = Exam('physics', 'Einstein', 'godlike', 1000)
f.gift()
f.drugs()
