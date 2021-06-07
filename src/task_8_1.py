from typing import NewType

n_type  = NewType('n' , int) # параметр целого типа 
def fact2 (n: n_type) -> int:
    factrial_nummber = 1
    if n % 2 == 0:
        fact2_list = [number for number in range(1, n) if number % 2 == 0]
    else:
        fact2_list = [number for number in range(1, n) if number % 2 != 0]

    for  value in fact2_list:
        factrial_nummber *= value
    return factrial_nummber


