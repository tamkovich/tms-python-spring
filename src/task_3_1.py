print("введите число для определения делиться оно без остатеа или нет:")
number = int(input())
if number % 1000 == 0:
    print("millennium")
else:
    print(number/1000)

## второй пункт задания

print("введите чоичество гостей которые придут на свадьбу:")
count = int(input())
if count > 50 :
    print("ресторан")
elif count > 20 and count <=50:
    print("кофе")
else:
    print("дом")


## 3-й пункт
line = "01234567890"
if len(line) > 10 :
    new_line = line + "!!!"
    print(new_line)
else:
    print(line[1])


## 4-й пункт
line_4 = "123416789"
midle_line = int(len(line_4)/2)
print(f"центральный символ - {line_4[midle_line]}")
if line_4[0] == line_4[midle_line]:
    print(f"первый символ совпал с центральным \n  новая строка - 111{line_4[1:-1]}")
