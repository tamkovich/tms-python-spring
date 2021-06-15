""" Дан список целых чисел.
Создать новый список, каждый элемент которого равен исходному элементу
умноженному на -2 """

# for loop
list_b = [-3, -2, -1, 0, 1, 2, 3,  4, 5, 6, 7, 8, 9, 10, 11]
a = -2
c = 0
list_c = []
for i in list_b:
    c = i * a
    list_c.append(c)
print(list_c)

# while loop
li_li = [-3, -2, -1, 0, 1, 2, 3,  4, 5, 6, 7, 8, 9, 10, 11]
new_li = []
b = -2
j = 0
k = 0
while True:
    if j <= len(li_li) - 1:
        k = b * li_li[j]
        j += 1
        new_li.append(k)
    else:
        break
print(new_li)
