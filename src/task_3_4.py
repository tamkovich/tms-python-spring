# 4) Ввести строку. Вывести на экран букву, которая находится в середине этой
# строки. Также, если эта центральная буква равна первой букве в строке, то создать и
# вывести часть строки между первым и последним символами исходной строки
# (подсказка: для получения центральной буквы, найдите длину строки и разделите
# ее пополам. Для создания результирующий строки используйте срез)
dream = input("Опишите вашу мечту:")
k = int(len(dream)/2)
print(dream[k])
if dream[k] == dream[0]:
    dream_1 = dream.split(' ')
    print(dream_1[1:-1])
    result = ' '.join(dream_1[1:-1])
    print(result)
