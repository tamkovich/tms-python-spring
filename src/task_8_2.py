"""
Создать lambda функцию, которая принимает на вход неопределенное
количество именных аргументов и выводит словарь с ключами удвоенной
длины. {‘abc’: 5} -> {‘abcabc’: 5}

"""
print((lambda **kwargs:
       {f"{key + key} : {value}" for key, value in kwargs.items()})
      (int=1, begin=2, string=4, boolean=5, float=6))
