a = [1, 2, 3, 4]
b = [5, 6, 7, 8, 9]
print(id(a))
print(id(b))
b = a
print(id(a))
print(id(b))
b.append(5)
print(b)
print(a)
