# Homework - 05
# task_5_8: В заданной строке расположить в обратном порядке все слова. Разделителями
# слов считаются пробелы. [02-7.2-HL08]
st = "мой дядя самых честных правил"
temp_list = st.split(" ")
temp_list2 = []
while temp_list:
    a = temp_list.pop()
    temp_list2.append(a)
new_st = " ".join(temp_list2)
print(new_st)
