# alpha-beta-pruning-Tic-Tac-Toe-Game-Bot
Course Design of Introduction to Artificial Intelligence

## I. Basic Program Overview
This program is a Tic Tac Toe game bot (Botzone challenge: Tic Tac Toe), utilizing the minimax algorithm with alpha-beta pruning to determine the optimal moves in the game. The basic idea is to simulate all possible moves in the game, evaluate each position, and find the best moves for both players. The alpha-beta pruning technique is employed to optimize the algorithm by trimming branches in the game tree that do not affect the final decision.

The program runs smoothly during testing, demonstrating fast execution speed. It can compete evenly with the top-ranked program on the leaderboard.

## II. Specific Implementation Algorithm
The program is developed using the Python language on the Google Colaboratory platform.

The Tic Tac Toe game is played on a 3x3 board, with players represented by "X" and "O," and empty cells indicated by a space " ".

The core of the algorithm is the minmax function. It recursively evaluates the game state by simulating possible moves and assigning scores to each position. Scores are determined as follows: 1 for "X" winning, -1 for "O" winning, and 0 for a draw.

Alpha-beta pruning is implemented in the minmax function to eliminate unnecessary branches in the game tree. The alpha and beta parameters represent the best values found by maximizing and minimizing players, respectively. If the score of a branch is outside the current alpha-beta window, that branch is pruned, saving computational resources.

The best_move function iterates over all empty cells on the board, simulating each move of the "X" player and using the minimax algorithm to determine the best move by selecting the move with the highest score.

In the direct runnable version of the program, the main function allows the player to make moves and interact with the program. The game loop continues until there is a winner or a draw.

## III. Final Results and Future Improvements
Program Test Results

The direct runnable version of the program allows normal gameplay between the player and the program. The player can input moves, and the program responds quickly, calculating the best move to counter. The program visualizes the board state after each move.

The Botzone version of the program is submitted to Botzone for testing. The program runs well and can achieve a draw even when competing against the top-ranked program on the leaderboard.

Future Improvements

Algorithm Adjustment: Consider adopting more advanced search algorithms, such as using a pre-trained neural network model as an evaluation function or incorporating Monte Carlo tree search, to more effectively handle large-scale board scenarios.

Depth Adjustment: The current exploration depth of the minimax function is set to 3 layers. Adjusting this depth may impact the performance and resource usage of the bot.

Heuristic Evaluation: Introduce a heuristic evaluation function to further optimize the algorithm, especially for larger game trees.
