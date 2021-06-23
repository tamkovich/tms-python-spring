""" Задание 8.2
Даны три слова. Выяснить, является ли хоть одно из них палиндромом
("перевертышем"), т. е. таким, которое читается одинаково слева направо и
справа налево. (Определить функцию, позволяющую распознавать слова
палиндромы.)"""


def is_palindrome(s: str) -> bool:
    return s.upper() == s.upper()[::-1]


words = ["Deed", "level", "Campus", "Linux", "peep", "noon", "TeachMeSkills", "Racecar"]

for word in words:
    print(f"'{word}' - {'is palindrome' if is_palindrome(word) else 'is not palindrome'}")
