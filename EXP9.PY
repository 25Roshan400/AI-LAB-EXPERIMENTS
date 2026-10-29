def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True

        if all(board[j][i] == player for j in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("TIC-TAC-TOE GAME")
    print("Enter row and column numbers from 1 to 3.")

    for turn in range(9):
        print_board(board)
        print("Player", current_player, "'s turn")

        try:
            row = int(input("Enter row (1-3): ")) - 1
            col = int(input("Enter column (1-3): ")) - 1
        except ValueError:
            print("Invalid input! Enter numbers only.")
            continue

        if not (0 <= row < 3 and 0 <= col < 3):
            print("Invalid position! Try again.")
            continue

        if board[row][col] != " ":
            print("Position already occupied! Try again.")
            continue

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print("Player", current_player, "wins!")
            return

        current_player = "O" if current_player == "X" else "X"

    print_board(board)
    print("Game Draw!")


tic_tac_toe()
