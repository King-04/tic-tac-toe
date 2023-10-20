def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]) or all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def is_board_full(board):
    return all([cell != " " for row in board for cell in row])

def play_tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player_idx = 0

    while True:
        print_board(board)
        row, col = map(int, input(f"Player {players[current_player_idx]}, enter your move (row[1-3] column[1-3]): ").split())

        if board[row - 1][col - 1] == " ":
            board[row - 1][col - 1] = players[current_player_idx]
            if check_winner(board, players[current_player_idx]):
                print_board(board)
                print(f"Player {players[current_player_idx]} wins!")
                break
            elif is_board_full(board):
                print_board(board)
                print("It's a draw!")
                break
            else:
                current_player_idx = 1 - current_player_idx
        else:
            print("Invalid move. Try again.")

play_tic_tac_toe()
