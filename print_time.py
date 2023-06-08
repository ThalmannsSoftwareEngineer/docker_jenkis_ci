"""Autor: Kevin Thalmann."""
import datetime


def current_time() -> None:
    """Print the current time."""
    print(F"Es ist {datetime.datetime.now().strftime('%H:%M:%S')} Uhr")  # noqa: T201


if __name__ == "__main__":
    current_time()
