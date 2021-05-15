list_1 = ['a','b','c']
list_2 = ['d','e','f']
list_1.insert(0, 'start_1')
print(list_1)
length = len(list_1)
list_1.insert(length, 'finish_1')
print(str(list_1) + '\n')

list_2.insert(0, 'start_2')
print(list_2)
length = len(list_2)
list_2.insert(length, 'finish_2')
print(str(list_2) + '\n')

list_3 = list_1.extend(list_2)
print('List_3:', list_3)