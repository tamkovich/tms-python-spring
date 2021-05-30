#Задание 2.02
# Создать два списка произвольного содержания.
# Добавить к каждому списку по одному элементу в конец и в начало.
# Расширить первый список вторым.
# Все изменения выводить на экран.
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