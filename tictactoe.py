def print_board(board):
     print("---------")
     for row in board:
         print(f"| {' '.join(row)} |")
     print("---------")

def check_winner(board, symbol):
    for i in range(3):
        if all(board[i][j] == symbol for j in range(3)):
            return True
        if all(board[j][i] == symbol for j in range(3)):
            return True
        if all(board[i][i] == symbol for i in range(3)):
            return True
        if all(board[i][2 - i] == symbol for i in range(3)):
            return True
        return False

def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True


def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print_board(board)

    current_player = "X"
    while True:
        try:
            user_input = input("Enter the coordinates: ").strip()
            parts = user_input.split()

            if len(parts) != 2:
                print("You should enter numbers!")
                continue

            row, col = int(parts[0]), int(parts[1])

            if not (1 <= row <= 3 and 1 <= col <= 3):
                print("Coordinates should be from 1 to 3!")
                continue

            r, c = row - 1, col - 1

            if board[r][c] != " ":
                print("This cell is occupied! Choose another one!")
                continue

            board[r][c] = current_player
            print_board(board)

            if check_winner(board, current_player):
                print(f"{current_player} wins")
                break
            elif is_board_full(board):
                print("Draw")
                break

            current_player = "O" if current_player == "X" else "X"

        except ValueError:
            print("You should enter numbers!")
if __name__ == "__main__":
 main()