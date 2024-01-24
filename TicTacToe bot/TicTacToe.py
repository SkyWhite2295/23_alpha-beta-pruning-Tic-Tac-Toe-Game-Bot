import math

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def is_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(row[col] == player for row in board):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

def minimax(board, depth, maximizing_player, alpha, beta):
    if is_winner(board, "O"):
        return -1
    if is_winner(board, "X"):
        return 1
    if is_board_full(board):
        return 0

    if maximizing_player:
        max_eval = -math.inf
        for i, j in get_empty_cells(board):
            board[i][j] = "X"
            eval = minimax(board, depth + 1, False, alpha, beta)
            board[i][j] = " "
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for i, j in get_empty_cells(board):
            board[i][j] = "O"
            eval = minimax(board, depth + 1, True, alpha, beta)
            board[i][j] = " "
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)

    for i, j in get_empty_cells(board):
        board[i][j] = "X"
        move_val = minimax(board, 3, False, -math.inf, math.inf)
        board[i][j] = " "

        if move_val > best_val:
            best_move = (i, j)
            best_val = move_val

    return best_move

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]

    while True:
        print_board(board)

        user_row = int(input("Enter row (0, 1, or 2): "))
        user_col = int(input("Enter column (0, 1, or 2): "))

        if board[user_row][user_col] != " ":
            print("Cell already taken. Try again.")
            continue

        board[user_row][user_col] = "O"

        if is_winner(board, "O"):
            print_board(board)
            print("You win!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        print("Computer's turn...")
        computer_row, computer_col = best_move(board)
        board[computer_row][computer_col] = "X"

        if is_winner(board, "X"):
            print_board(board)
            print("Computer wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

if __name__ == "__main__":
    main()