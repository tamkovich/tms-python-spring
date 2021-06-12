# Задание 5.08
# В заданной строке расположить в обратном порядке все слова.
# Разделителями слов считаются пробелы. [02-7.2-HL08]

s = "I use both iPhone and Samsung. A great leader has to be flexible /D.Trump/"

print(f"Source string:\n{s}\n")

words = s.split(" ")
s = " ".join(words[::-1])

print(f"Reversed string: \n{s}")
