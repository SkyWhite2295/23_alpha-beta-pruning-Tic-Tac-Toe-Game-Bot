import json
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
        move_val = minimax(board, 2, False, -math.inf, math.inf)
        board[i][j] = " "

        if move_val > best_val:
            best_move = (i, j)
            best_val = move_val

    return best_move

all_data = json.loads(input())

all_requests = all_data["requests"]
my_id = all_requests[0]["x"] == -1

my_data = [[None, None, None] for _ in range(3)]

for i in range(len(all_requests)):
    my_request = all_requests[i]
    if my_request["x"] >= 0:
        my_data[my_request["x"]][my_request["y"]] = not my_id

curr_request = all_requests[-1]

if curr_request["x"] >= 0:
    my_data[curr_request["x"]][curr_request["y"]] = not my_id

# Initialize the board
board = [[" " for _ in range(3)] for _ in range(3)]

# Update the board based on opponent's moves
for move in all_data["requests"]:
    board[move["x"]][move["y"]] = "O"

# Update the board based on your moves
for move in all_data["responses"]:
    board[move["x"]][move["y"]] = "X"

Best_move = best_move(board)
best_move_dict = {"x": Best_move[0], "y": Best_move[1]}

print(json.dumps({"response": best_move_dict}))