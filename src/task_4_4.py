"""  Дан список. Создать новый список, сдвинутый на 1 элемент влево
Пример: 1 2 3 4 5 ->  2 3 4 5 1 """

# for loop
list_4_4 = [1, 2, 3, 4, 5]
new_list = []
for i in range(len(list_4_4) - 1):
   new_list = list_4_4.pop()
   list_4_4.insert(0, new_list)
print(list_4_4)

# while loop
list_jjj = [10, 20, 30, 40, 50]
new_jjj = []
j = 0
while j < len(list_jjj) - 1:
    new_jjj = list_jjj.pop()
    list_jjj.insert(0, new_jjj)
    j += 1
print(list_jjj)
