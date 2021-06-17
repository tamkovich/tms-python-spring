"""  Дан список целых чисел. Подсчитать сколько четных чисел в списке. """

# for loop
list_integer = [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
s = []
i = 0
for i in list_integer:
    if i % 2 == 0:
        s.append(i)
        i += 1
print(len(s))

# while loop
li_lu = [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
lis_c = []
b = 0
j = 0
while j <= len(li_lu) - 1:
    b = li_lu[j]
    j += 1
    if b % 2 == 0:
        lis_c.append(b)
print(len(lis_c))
