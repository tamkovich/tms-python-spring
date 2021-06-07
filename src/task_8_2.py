def polindrom(word):
    return word == word[::-1]


if __name__ == "__main__":
    word = "дед"
    if polindrom(word):
        print("слово полиндром")
    else:
        print("слово не является полиндромом")
