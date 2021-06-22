# Даны три слова. Выяснить, является ли хоть одно из них палиндромом ("перевертышем"),
# т. е. таким, которое читается одинаково слева направо и справа налево.
# (Определить функцию, позволяющую распознавать слова палиндромы.)[03-10.32]


def palindrom(words):
    count = 0
    for word in words:
        new_word = word[:: -1]
        if new_word == word:
            count += 1
    return count != 0


spisok_slov = ['amam', 'privet', 'okoko']
print(palindrom(spisok_slov))
