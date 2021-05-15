a = [1, 2, 3, 4]
b = []
b = a                         # create link from list a to list b
print(id(a), id(b))
c = b.append(5)
print(str(a) + '\n' + str(b))
