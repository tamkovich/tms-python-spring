print("введите чоичество гостей которые придут на свадьбу:")
count = int(input())
if count > 50 :
    print("ресторан")
elif count > 20 and count <=50:
    print("кофе")
else:
    print("дом")
