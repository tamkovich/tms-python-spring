from datetime import timedelta
import time


def step_pomodoro(focus_time: int, u_break: int, cycles: int):
    # Expected type 'Iterator' по итогу идентифицирует как Unresolved reference 'Iterator' ?
    """Ф-ция пошагового выполнения. yield - как доп.элем.управл.: старт таймеров"""
    for i in range(cycles):
        print(f"Цикл № {i+1}")
        yield countdown(focus_time)
        if cycles == i + 1:
            break
        else:
            print(f"Перерыв № {i + 1}")
            yield countdown(u_break)
    yield print("Happy end!")


def countdown(minutes):
    """Ф-ция обратного отсчета."""
    total_seconds = minutes * 60
    for j in range(total_seconds, 0, -1):
        print(f"Оставшееся время: {str(timedelta(seconds=j))}")
        time.sleep(1)


def log_func(first_name: str, last_name: str, focus_time: int, u_break: int, cycles: int) -> None:
    """Ф-ция логирования запусков помодоро."""
    with open('src/log.txt', "a") as f:
        f.write(f"{last_name} {first_name} focus time: {focus_time} "
                f"break: {u_break} cycles: {cycles}\n")
