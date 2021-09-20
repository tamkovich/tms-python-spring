"""
Создать два списка произвольного содержания.
Добавить к каждому списку по одному элементу
в конец и в начало. Расширить первый список вторым.
Все изменения выводить на экран.
"""
name = ["Yosu", "ksuha"]
age = [25, 26]
name.insert(0, "Vera")
name.append("Luba")
age.insert(0, 24)
age.append(28)
print(name)
print(age)
name.extend(age)
print(name)
