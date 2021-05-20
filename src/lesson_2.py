firstname = 'Ivan'  # z_2_01
lastname = 'Ivanov'
age = '35'
print("Привет, меня зовут {} {}, мне {} лет".format(firstname, lastname, age))

cars = ['mers', 'audi', 'bmw']  # z_2_02
students = ['ihor', 'masha', 'sasha']
cars.append('ford')
print(cars)
cars.insert(0, 'fiat')
print(cars)
students.append('ivan')
print(students)
students.insert(0, 'gosha')
print(students)
cars.extend(students)  # cars += students
print(cars)
type(cars)

cars = ["audi", "bmw"]  # z_2_03
print(cars)
fruts = ("apple", "orange")
print(fruts)
dict_1 = {
    fruts: cars
    }
print(dict_1)

dict_2 = {
    fruts: fruts  # if cars - error
    }
print(dict_2)

a = [1, 2, 3, 4]  # z_2_04
b = []
print(id(a))
print(id(b))
b = a
print(id(a))
print(id(b))
b.append(999)
print(a)
print(b)
