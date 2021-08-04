import csv

# with open("users.csv") as f:
#     reader = csv.reader(f)
#     for line in reader:
#         print(line)


# with open("users.csv", "a") as f:
#     writer = csv.writer(f)
#     writer.writerow([6, "denis@gmail.com", "denis", "tam", 10])



email = "denis@gmail.com"
users = []
with open("users.csv", "r") as f:
    reader = csv.reader(f)

    for line in reader:
        if line[1] == email:
            line[-1] = "asdfghjkl"
        users.append(line)


with open("users.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(users)
