dict_value_home = {
    "test": "test_value",
    "europpe": "eur",
    "dollar": "usd",
    "ruble": "rub",
}

dict_new = {}

for key in dict_value_home.keys():
    dict_new[key + str(len(key))] = dict_value_home[key]
print(dict_new)

dict_new_1 = {}
i = 0
list_key = list(dict_value_home.keys())

while True:
    dict_new_1.setdefault(
        list_key[i] + str(len(list_key[i])), dict_value_home[list_key[i]]
    )
    i += 1
    if i > 3:
        break

print(dict_new_1)
