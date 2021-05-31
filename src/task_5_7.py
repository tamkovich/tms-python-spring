matrix = [
    [1, 2, 33, 4],
    [4, 2, 3, 44],
    [1, 2, 31, 4],
    [1, 2, 3, 41],
]
for index, i in enumerate(matrix):
    maxx = max(i)
    index_max = i.index(maxx)
    temp = i.pop(index)
    i.insert(index, maxx)
    i[index_max] = temp
    print(matrix[index])

print(matrix)
