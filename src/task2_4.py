a = [1, 2, 3, 4]
b = []
print(a, b)
b = a
print(id(a), id(b))
b.append(6)
print(a, b)
