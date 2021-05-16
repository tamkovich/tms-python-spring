first_list = ['правят']
first_list.append('этим миром')
print(first_list)
first_list.insert(0,'Котики')
print(first_list)
second_list = ['Котики']
second_list.append('рулят')
print(second_list)
second_list.insert(0,'и конечно же')
print(second_list)
first_list.extend(second_list)
print(first_list)


