#Задание 2.01
firstname = "Никита"
lastname = " Семячко"
age = "26"
i = "Привет, меня  зовут " + firstname + lastname +  ", " + "мне " + age + " лет"
print(i)
print(len(i))
print(age.isdigit())
print(i.isdigit())
print(i.find("меня"))
print(firstname[3:])
k = "Hello world"
print(k[0:7:3])
print(lastname[0: 5:2])
l ="My " "{} {} {}".format("Hello","Sweet", "World" )
print(l)
#Задание 2.02
songs = ["creep", "hurricane", "war"]
music = ["rock", "rnb", "dnb" ]
songs.insert(0, "pretending")
songs.append("cry")
music.append("metal")
music.insert(0, "pop")
print(songs)
print(music)
songs.extend(music)
print(songs)
#Задание 2.03
avto = ["ford", "honda"]
motor = ("бензин","дизель")
slvr = {motor:avto}
print(slvr)
slvrt ={("dodge","ford"):"USA","honda":"JAPAN"}

print(slvrt)
print(type(slvrt))
print(list('he'))
print(id(1))
#Задание 2.04
a = [1, 2, 3, 4]
b = []
print(id(a))
print(id(b))
b = a
print(id(a))
print(id(b))
b.append(45)
print(a)
print(b)
