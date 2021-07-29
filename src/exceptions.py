list_ValueError = []
list_KeyError = []
list_ZeroDivisionError = []


def add_error_v(v: ValueError) -> None:
    """Ф-ция добавляет ValueError в соответствующий список """
    list_ValueError.append(v)


def add_error_k(k: KeyError) -> None:
    """Ф-ция добавляет KeyError в соответствующий список """
    list_KeyError.append(k)


def add_error_z(z: ZeroDivisionError) -> None:
    """Ф-ция добавляет ZeroDivisionError в соответствующий список """
    list_ZeroDivisionError.append(z)


def print_error() -> None:
    print(f"Было {len(list_ValueError)} ValueError: {list_ValueError}")
    print(f"Было {len(list_KeyError)} KeyError: {list_KeyError}")
    print(f"Было {len(list_ZeroDivisionError)} ZeroDivisionError: {list_ZeroDivisionError}")
