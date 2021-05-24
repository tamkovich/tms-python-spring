print("введите число для определения делиться оно без остатеа или нет:")
number = int(input())
if number % 1000 == 0:
    print("millennium")
else:
    print(number/1000)
