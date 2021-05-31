from datetime import datetime
from datetime import time

list_raspisanie_poezdob = [
    {
        "number_poezd": 13,
        "punkt_pribitiya": "Минск",
        "time_pribitiya": datetime(2021, 1, 11, 20, 35),
        "punkt_otpravki": "Гродно",
        "time_otpravki": datetime(2021, 1, 11, 16, 40),
    },
    {
        "number_poezd": 14,
        "punkt_pribitiya": "Брест",
        "time_pribitiya": datetime(2021, 5, 16, 14, 31),
        "punkt_otpravki": "Минск",
        "time_otpravki": datetime(2021, 5, 16, 7, 00),
    },
    {
        "number_poezd": 747,
        "punkt_pribitiya": "Вильнус",
        "time_pribitiya": datetime(2021, 1, 21, 5, 40),
        "punkt_otpravki": "Афины",
        "time_otpravki": datetime(2021, 1, 19, 16, 40),
    },
]
itime = time(7, 20)
second = (itime.hour * 60 * 60) + (itime.minute * 60)
for dict_poezd in list_raspisanie_poezdob:
    delta = dict_poezd["time_pribitiya"] - dict_poezd["time_otpravki"]
    if delta.seconds > second:
        print(
            f"номер поезда {dict_poezd['number_poezd']}"
        )
        print(
            f"-время отправки {dict_poezd['time_otpravki']}"
        )
        print(
            f"-время прибытия {dict_poezd['time_pribitiya']}"
        )
        print(
            f"-пункт отправки {dict_poezd['punkt_otpravki']}"
        )
        print(
            f"-пункт назначения {dict_poezd['punkt_pribitiya']}\n-время в пути {delta}"
        )
