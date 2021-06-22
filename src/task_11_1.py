"""
Создать пять классов описывающие реальные объекты.
Каждый класс должен содержать минимум три приватных атрибута, конструктор,
геттеры и сеттеры для каждого атрибута, два метода.
"""


class Airplane:
    """
    Class airplane have 4 private atributes
    В каждом классе отдельно созданы функции вывода информации
    """

    def __init__(self, weight, speed, name, passengers, engine, types):
        self.weight = weight
        self.speed = speed
        self.__name = name
        self.__passengers = passengers
        self.__engine = engine
        self.__type = types

    def engine_woof(self):
        return 'Engine work fine'

    def airplane_country(self):
        return 'Go to Moscow!'

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_passengers(self):
        return self.__passengers

    def set_passenger(self, passengers):
        self.__passengers = passengers

    def get_engine(self):
        return self.__engine

    def set_engine(self, engine):
        self.__engine = engine

    def get_type(self):
        return self.__type

    def set_type(self, types):
        self.__type = types

    def info(self):
        return (f'All characters:\n1.weight - {airplane.weight}\n'
                f'2.speed - {airplane.speed}\n'
                f'3.name - {airplane.get_name()} {airplane.set_name("Airbus")}\n'
                f'But NO! This is - {airplane.get_name()}\n'
                f'4.places - {airplane.get_passengers()}\n'
                f'5.engine - {airplane.get_engine()}\n6.type - {airplane.get_type()}')


class Car:
    """
    Родительский класс который будем наследовать
    в классe BMW
    """

    def __init__(self, body: str, engine: str, type_car: str, count=4, doors=5):
        self.__count = count
        self.doors = doors
        self.engine = engine
        self.__body = body
        self.__type_car = type_car

    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, body):
        self.__body = body

    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self, count):
        self.__count = count

    @property
    def type_car(self):
        return self.__type_car

    @type_car.setter
    def type_car(self, type_car):
        self.__type_car = type_car

    def car_brah(self):
        return 'I created my first car!'

    def car_working(self):
        if self.body == 'sedan':
            return 'Sedan - Nice body'
        else:
            return 'So - So'

    def info(self):
        return f'{self.type_car} {self.doors} {self.count} {self.engine} {self.body}'


class BMW(Car):
    """
    Наследование через Super Class
    """

    def __init__(self, body: str, country: str, weight: int,
                 count: int, doors: int,
                 engine: str, power: int,
                 turbo: bool, fuel: str, type_car: str):
        super().__init__(body, engine, type_car, count, doors)
        self.__power = power
        self.weight = weight
        self.__engine = engine
        self.country = country
        self.__turbo = turbo
        self.fuel = fuel

    def car_work(self):
        return 'BMW work? Its great!'

    def check_engine(self):
        return 'Oh no, going to service'

    @property
    def power(self):
        return self.__power

    @power.setter
    def power(self, power):
        self.__power = power

    @property
    def engine(self):
        return self.__engine

    @engine.setter
    def engine(self, engine):
        self.__engine = engine

    @property
    def turbo(self):
        return self.__turbo

    @turbo.setter
    def turbo(self, turbo):
        self.__turbo = turbo

    def info_bmw(self):
        return (f'1.body - {car.body}\n2.country - {bmw.country}\n'
                f'3.weight - {bmw.weight}\n'
                f'4.doors - {car.doors}\n5.count - {car.count}\n6.engine - {bmw.engine}\n'
                f'7.horse power - {bmw.power}\n8.Turbo - {bmw.turbo}\n'
                f'9.gas - {bmw.fuel}\n10.type - {car.type_car}')


class Human:
    """
    Родительский класс который будем наследовать
    в классах Techer, Pupil
    """
    name: str
    last_name: str
    age: int
    sex: str

    def __init__(self, name: str, last_name: str, age: int, sex: str):
        self.__name = name
        self.__last_name = last_name
        self.__age = age
        self.sex = sex

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name):
        self.__last_name = last_name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age


class Pupil(Human):
    def __init__(self, name: str, last_name: str, age: int, sex: str,
                 class_number: str, favorite_lesson: str,
                 school_number: int):
        super().__init__(name, last_name, age, sex)
        self.__class_number = class_number
        self.__favorite_lesson = favorite_lesson
        self.__school_number = school_number

    @property
    def class_number(self):
        return self.__class_number

    @class_number.setter
    def class_number(self, class_number):
        self.__class_number = class_number

    @property
    def favorite_lesson(self):
        return self.__favorite_lesson

    @favorite_lesson.setter
    def favorite_lesson(self, favorite_lesson):
        self.__favorite_lesson = favorite_lesson

    @property
    def school_number(self):
        return self.__school_number

    @school_number.setter
    def school_number(self, school_number):
        self.__school_number = school_number

    def pupil_age(self):
        return 'age != 18)'

    def pupil_work(self):
        return 'Pupil is not working'

    def info(self):
        return (f'Name - {pupil.name}\nlast name - {pupil.last_name}\n'
                f'age - {pupil.age}\nsex - {pupil.sex}\n'
                f'Class - {pupil.class_number}\n'
                f'lesson - {pupil.favorite_lesson}\nSchool - {pupil.school_number}')


class Teacher(Human):
    def __init__(self, name: str, last_name: str, age: int, sex: str, lesson: str,
                 school_number: int, class_number: str):
        super().__init__(name, last_name, age, sex)
        self.__lesson = lesson
        self.__school_number = school_number
        self.__class_number = class_number

    @property
    def lesson(self):
        return self.__lesson

    @lesson.setter
    def lesson(self, lesson):
        self.__lesson = lesson

    @property
    def school_number(self):
        return self.__school_number

    @school_number.setter
    def school_number(self, school_number):
        self.__school_number = school_number

    @property
    def class_number(self):
        return self.__class_number

    @class_number.setter
    def class_number(self, class_number):
        self.__class_number = class_number

    def stand_up(self):
        return f'Class please stand up'

    def info(self):
        return (f'Name - {teacher.name}\nlast name - {teacher.last_name}\n'
                f'age - {teacher.age}\nsex - {teacher.sex}\n'
                f'lesson - {teacher.lesson}\nSchool - {teacher.school_number}\n'
                f'Class - {teacher.class_number}')


"""
Вывод информации объектов
"""
if __name__ == '__main__':
    print("--------------- Airplane -----------------")
    airplane = Airplane(10000, 1200, 'Boeing', 1000, 'Rolls-Royce', 'passenger air')
    print(airplane.info(), airplane.engine_woof(),
          airplane.airplane_country(),
          sep='\n')

    print("--------------- We made Cars -----------------")
    car = Car('sedan', 'diesel', 'City car')
    print(car.info(), car.car_brah(), car.car_working(),
          sep='\n')

    print("--------------- BMW 525 -----------------")
    bmw = BMW(car.body, 'Germany', 2200, car.doors, car.count, 'gas engine',
              200, True, 'petrol', car.type_car)
    bmw.power = 250
    print(bmw.info_bmw(), bmw.car_work(), bmw.check_engine(),
          sep='\n')

    print("--------------- Teacher -----------------")
    teacher = Teacher('Maria', 'Ivanovna', 35, 'Women', 'Biologi', 42, '9A')
    print(teacher.info(), teacher.stand_up(), sep='\n')

    print("--------------- Pupil -----------------")
    pupil = Pupil('Ivan', 'Ivanov', 16, 'Man', '9B', 'Informatic', 54)
    print(pupil.info(), pupil.pupil_age(), pupil.pupil_work(),
          sep='\n')
