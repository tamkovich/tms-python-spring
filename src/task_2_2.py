# Task 1
string = "Hello Python"
string_result = string[2]
print(string_result)

# Task 2
string = "Hello Python"
string_result = string[-2]
print(string_result)

# Task 3
string = "Hello Python"
string_result = string[0: 5]
print(string_result)

# Task 4
string = "Hello Python"
string_result = string[: -2]
print(string_result)

# Task 5 Решил использовать этот метод, так как это проще всего)
string = "Hello Python"
string_result = ""
i = 0
while i < len(string):
    string_result = string_result + string[i]
    i = i + 2
print(string_result)
