# 1. Создать пять классов описывающие реальные объекты. Каждый класс
# должен содержать минимум три приватных атрибута, конструктор, геттеры
# и сеттеры для каждого атрибута, два метода.


import random


class Person:
    def __init__(self, age, gender, height, weight, hair, eyes):
        self.words_dictionnary = {}
        self.__age = age
        self._gender = gender
        self.__height = height
        self.__weight = weight
        self.__hair = hair
        self.__eyes = eyes

    @property
    def age(self):
        print("Запрашиваем возраст...")
        return self.__age

    @age.setter
    def age(self, age):
        if age < 125:
            self.__age = age
            print(f"Возраст успешно изменен. Возраст - {self.__age} лет.")
        else:
            print("Пробирочные люди старше 125 лет подлежат эвтаназии.")

    @property
    def height(self):
        print("Запрашиваем рост...")
        return f"{self.__height} сантиметров."

    @height.setter
    def height(self, height):
        if 250 < height < 30:
            print("Таких людей не бывает")
        else:
            self.__height = height
            print(f"Рост успешно изменен. Рост - {self.__height} сантиметров.")

    @property
    def weight(self):
        print("Запрашиваем вес...")
        print("Попроси красиво.")
        if input() == "Пожалуйста":
            return f"Ладно. Так и быть. {self.__weight} килограмм."
        else:
            return "Давай досвиданья."

    @weight.setter
    def weight(self, weight):
        self.__weight = weight

    @property
    def gender(self):
        print("Проверяем...")
        return self.__gender

    @gender.setter
    def gender(self, gender):
        print("Операция по смене пола завершена. Успешно ли - вопрос.")
        zero_or_one = random.randint(0, 1)
        if zero_or_one == 1:
            self.__gender = gender
            print(f"Все прижилось. Теперь особь - {self.__gender}.")
        else:
            print("Извините, все пришитое отвалилось. Попробуйте еще.")

    @property
    def hair(self):
        print("Запрашиваем...")
        return f"{self.__hair} волосы."

    @hair.setter
    def hair(self, hair):
        permitted_colors = (
            "красные", "зеленые", "синие", "белые", "серо-буро-малиновые", "фисташковые"
        )
        if hair in permitted_colors:
            self.__hair = hair
            print(f"Волосы перекрашены в {self.__hair}.")
        else:
            print(
                "Вашего цвета нет в Высочайшем реестре Пробирочного царства.\nТак краситься нельзя!"
            )

    @property
    def eyes(self):
        print("Запрашиваем...")
        return f"{self.__hair} глаза."

    @eyes.setter
    def eyes(self, eyes):
        random_colors = (
            "красные", "зеленые", "синие", "белые", "серо-буро-малиновые", "фисташковые"
        )
        random_color = random.choice(random_colors)
        self.__eyes = random_color
        print(
            f'Глаза теперь {self.__eyes}. НЕ {eyes}')

    def learn_a_word(self):
        word = input("Я могу учить новые слова! Научи меня новому слову!")
        word = word.title()
        word_meaning = input(f"{word}... А что это такое?")
        if "это" in word_meaning:
            word_meaning = word_meaning.replace("это", "")
        word_meaning = word_meaning.lower()
        self.words_dictionnary[word] = word_meaning
        print(f"Теперь я знаю! {word} - это {word_meaning}!")

    def tell_me_something(self):
        words_dictionnary = self.words_dictionnary
        try:
            word, meaning = random.choice(list(words_dictionnary.items()))
            word = word.lower()
            print(f"А ты знал, что {word} - это {meaning}?")
        except AttributeError:
            print("А я ничего не знаю")


class Student(Person):
    def __init__(self, age, gender, height, weight, hair, eyes, faculty=None, score=0):
        super(Student, self).__init__(age, gender, height, weight, hair, eyes)
        self.__faculty = faculty
        self.__score = score

    @property
    def faculty(self):
        gender = self._gender
        if self.__faculty:
            return f"Факультет - {self.__faculty}"
        elif gender == "мужчина":
            return "Особь болтается сама по себе. Ей угрожает армия."
        elif gender == "женщина":
            return "Особь болтается сама по себе. Ей угрожает панель."
        else:
            return "Особь болтается сама по себе."

    @faculty.setter
    def faculty(self, faculty):
        self.__faculty = faculty
        print(f"Поздравляем с поступлением на {self.__faculty}!")

    @faculty.deleter
    def faculty(self):
        del self.__faculty
        self.__faculty = None
        print("Студента отчислили.")

    @property
    def score(self):
        faculty = self.__faculty
        if faculty:
            self.__score = len(self.words_dictionnary)
            return self.__score
        else:
            return "Особь не нигде не числится. Среднего балла у нее нет."

    @score.setter
    def score(self, score):
        self.__score = len(self.words_dictionnary)
        print(
            f"Средний балл - {self.__score}."
            f"\nВаши попытки установить балл {score} безуспешны."
            f"\nЛучше научите студента новым словам.")

    def miss_a_class(self):
        word_to_forget = random.choice(list(self.words_dictionnary.keys()))
        del self.words_dictionnary[word_to_forget]
        print("Студент прогулял уроки и кое-что забыл.")

    def session(self):
        word_to_ask = input("Что вы хотели у меня спросить?").title()
        result = self.words_dictionnary.get(word_to_ask, "Это мы не проходили!")
        print(result)


class Employee(Person):
    def __init__(self, age, gender, height, weight, hair, eyes, job, salary, experience):
        super(Employee, self).__init__(age, gender, height, weight, hair, eyes)
        self.__job = job
        self.__salary = salary
        self.__experience = experience
        self.work_hard_count = 0

    @property
    def job(self):
        return f"Особь - {self.__job}"

    @job.setter
    def job(self, job):
        self.__job = job
        print(f"Особь устроилась на работу. Теперь она {self.__job}")

    @job.deleter
    def job(self):
        self.__job = 'Безработный'
        print("Особь шагает на биржу труда")

    @property
    def experience(self):
        return self.__experience

    @experience.setter
    def experience(self, experience):
        self.__experience = experience

    @experience.deleter
    def experience(self):
        print("Опыт не пропьешь!")

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        if salary > self.__salary:
            print("Поздравляем с повышением зарплаты!")
        elif salary < self.__salary:
            print("Зарплата понизилась. Печаль.")
        else:
            print("Вы поменяли шило на мыло.")
        self.__salary = salary

    @salary.deleter
    def salary(self):
        if self.__job:
            print("Зарплата не может быть меньше МРОТ!")
        else:
            self.__salary = 0

    def work_hard(self):
        self.experience += 1
        self.age += 1
        self.work_hard_count += 1
        print("Особь ударно трудится")

    def ask_a_promotion(self):
        print("Особь просит повышения")
        if self.experience > 10 or self.work_hard_count > 3:
            responce = True
        else:
            responce = False
        if responce:
            self.__salary += self.__salary * 0.1
            print(f"Зарплата повышена. Теперь - {self.__salary}!")
        else:
            print("Повышение не положено")


class Teacher(Employee):
    data = {
        "Фланировать":
            "неспешная прогулка без какой-либо конкретной цели",
        "Стяжатель":
            "человек, который стремится к наживе, накоплению денег",
        "Пипидастр":
            "пушистая разноцветную метелку для смахивания пыли",
        "Пюпитр":
            "наклонная подставка для нот или книг",
        "Фраппировать":
            "неприятно поражать, ошеломлять",
        "Гаптофобия":
            "паническая боязнь прикосновений других людей",
        "Экивоки":
            "двусмысленные намеки",
        "Пертрубация":
            "событие, которое меняет привычный ход вещей и вводит в замешательство",
        "Транспарентный":
            "обе стороны максимально честны и ничего не скрывают",
        "Инсайт":
            "так говорят, когда человек внезапно проникает в самую суть чего-либо",
    }

    def __init__(
        self, age, gender, height, weight, hair, eyes, job, salary, experience, *student
    ):
        super(Teacher, self).__init__(
            age, gender, height, weight, hair, eyes, job, salary, experience
        )

        self.student = student

    def teach_students(self):
        for every_student in self.student:
            word_to_teach, meaning = random.choice(list(self.data.items()))
            every_student.words_dictionnary[word_to_teach] = meaning
        print("Я учил, как мог")

    def ask_students(self):
        for i, every_student in enumerate(self.student):
            if every_student.words_dictionnary:
                print(f"Отвечает студент номер {i + 1}")
                for k, v in every_student.words_dictionnary.items():
                    print(f"{k} - {v}.")
            else:
                print(f"Студент номер {i + 1} тупой и ничего не знает")


# 2. Создать класс Car. Атрибуты: марка, модель, год выпуска, скорость(по
# умолчанию 0). Методы: увеличить скорости(скорость + 5), уменьшение
# скорости(скорость - 5), стоп(сброс скорости на 0), отображение скорости,
# разворот(изменение знака скорости). Все атрибуты приватные.

class Car:
    def __init__(self, mark, model, year):
        self.__mark = mark
        self.__model = model
        self.__year = year
        self.__speed = 0

    @property
    def mark(self):
        return self.__mark

    @mark.setter
    def mark(self, mark):
        self.__mark = mark

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        self.__model = model

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        self.__year = year

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed):
        self.__speed = speed

    def encrease_speed(self):
        if self.__speed < 0:
            self.__speed -= 5
        elif self.__speed >= 0:
            self.__speed += 5
        print("быстрее!!!!")
        print(f"Скорость выросла до {self.__speed}")

    def reduce_speed(self):
        if self.__speed > 0:
            self.__speed -= 5
        elif self.__speed < 0:
            self.__speed += 5
        else:
            print("Машина стоит, в чем дело?")
        print("мееееедленнеее....")
        print(f"Скорость упала до {self.__speed}")

    def stop(self):
        self.__speed = 0
        print("Машина стоит")

    def turn(self):
        self.__speed = -self.__speed
        print("Машина развернулась в другую сторону.")
