""" Даны три слова. Выяснить, является ли хоть одно из них палиндромом
("перевертышем"), т. е. таким, которое читается одинаково слева направо и
справа налево. (Определить функцию, позволяющую распознавать слова
палиндромы.)[03-10.32]
"""
list_exp = ['ivavi', 'nana', 'opo']


def is_palindrom(word: str) -> bool:
    if word[::-1] == word:
        return True
    else:
        return False


for word in list_exp:
    print(f"{word} это палиндром? - {is_palindrom(word)}")
