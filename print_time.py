"""Autor: Kevin Thalmann."""
import datetime


def current_time() -> None:
    """Print the current time."""
    now = datetime.datetime.now()
    zeit = now.strftime("%H:%M:%S")
    print(F"Es ist {zeit}Uhr")  # noqa: T201


if __name__ == "__main__":
    current_time()
