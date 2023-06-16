"""Autor: Kevin Thalmann."""
import datetime


def current_time() -> None:
    """Print the current time."""
    print(F"Es ist {datetime.datetime.now().strftime('%H:%M:%S')} Uhr")  # noqa: T201


def print_chessboard() -> None:
    """Print a chessgame."""
    chessboard = [
        ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
        ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
        ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
    ]
    print("\n")  # noqa: T201
    print("   a b c d e f g h")  # noqa: T201
    print("  -----------------")  # noqa: T201
    for i in range(len(chessboard)):
        print(str(8 - i) + " |", end="")  # noqa: T201
        for j in range(len(chessboard[i])):
            print(chessboard[i][j] + "|", end="")  # noqa: T201
        print(" " + str(8 - i))  # noqa: T201
        print("  -----------------")  # noqa: T201
    print("   a b c d e f g h")  # noqa: T201
    print("\n")  # noqa: T201
    print("KevinThalmann")  # noqa: T201

if __name__ == "__main__":
    current_time()
    print_chessboard()
