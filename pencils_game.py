import random


def get_initial_pencils():
    while True:
        pencils_str = input("How many pencils would you like to use:\n")
        if not pencils_str.isnumeric():
            print("The number of pencils should be numeric")
            continue
        pencils = int(pencils_str)
        if pencils == 0:
            print("The number of pencils should be positive")
            continue
        if pencils < 0:
            print("The number of pencils should be numeric")
            continue
        return pencils


def get_first_player(player1, player2):
    while True:
        first = input(f"Who will be the first ({player1}, {player2}):\n")
        if first in (player1, player2):
            return first
        print(f"Choose between '{player1}' and '{player2}'")


def get_bot_move(pencils):
    # Выигрышная стратегия бота Jack
    if pencils % 4 == 0:
        return 3
    elif pencils % 4 == 3:
        return 2
    elif pencils % 4 == 2:
        return 1
    else:  # pencils % 4 == 1 (проигрышная позиция)
        return random.randint(1, min(3, pencils))


def get_player_move(pencils):
    while True:
        move_str = input()
        if move_str not in ("1", "2", "3"):
            print("Possible values: '1', '2' or '3'")
            continue
        move = int(move_str)
        if move > pencils:
            print("Too many pencils were taken")
            continue
        return move


def main():
    player1 = "John"
    player2 = "Jack"

    pencils = get_initial_pencils()
    current_player = get_first_player(player1, player2)

    while pencils > 0:
        print("|" * pencils)
        print(f"{current_player}'s turn!")

        if current_player == player2:
            move = get_bot_move(pencils)
            print(move)
        else:
            move = get_player_move(pencils)

        pencils -= move

        if pencils == 0:
            winner = player2 if current_player == player1 else player1
            print(f"{winner} won!")
            break

        current_player = player2 if current_player == player1 else player1


if __name__ == "__main__":
    main()