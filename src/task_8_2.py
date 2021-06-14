"""
Создать lambda функцию, которая принимает на вход неопределенное
количество именных аргументов и выводит словарь с ключами удвоенной
длины. {‘abc’: 5} -> {‘abcabc’: 5}

"""
print((lambda **kwargs:
       {f"{key + key} : {value}" for key, value in kwargs.items()})
      (int__=1, begin__=2, string__=4, boolean__=5, float__=6))
