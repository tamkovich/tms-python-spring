# Задание 5.07
# Дана целочисленная квадратная матрица.
# Найти в каждой строке наибольший элемент и
# поменять его местами с элементом главной диагонали.
# [02-4.2-ML22]

from random import randint

table = []
table_size = 10  # 2D array size

for row in range(table_size):
    temp_row = []
    for cell in range(table_size):
        temp_row.append(randint(10, 99))
    table.append(temp_row)

print("Source table: ")
for row in table:
    print(row)

print("\nMax elements in rows:")

for row_number, row in enumerate(table):
    max_cell = row[0]
    max_cell_number = 0
    for cell_number, cell in enumerate(row):
        if cell > max_cell:
            max_cell = cell
            max_cell_number = cell_number
    print(f"row {row_number}: max element {max_cell}, index {max_cell_number}")
    temp = row[row_number]
    row[row_number] = max_cell
    row[max_cell_number] = temp

print("\nThe table with elements replaced according to task:")
for row in table:
    print(row)
