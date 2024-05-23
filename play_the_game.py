from awale_board import *
from MCT import *
import sys

def print_board(board):
    print("Board State:")
    for i in range(len(board)):
        str = ""
        for j in range(len(board[i])):
            str +=f"{board[i][j]:2d} "
        print(f"\t[ {str}]")

def play_game(iterations):
    board = AwaleBoard()
    total_depth = 0
    num_moves = 0
    print_board(board.board)
    while not board.is_game_over():
        if board.current_player == 0:
            print(f"Player 0's turn number {num_moves}")
            move, avg_depth, move_evaluations = mcts_search(board, iterations)
            total_depth += avg_depth
            num_moves += 1
            print(f"Average search depth: {avg_depth:.3f}")
            print(f"Move evaluations: {move_evaluations}")
        else:
            print("Player 1's turn")
            move = random.choice(board.get_moves())

        print(f"chosen move: {move}")
        board.make_move(move)
        print_board(board.board)
        score0, score1 = board.get_score()
        print(f"Player:  0  1\nScore:  {score0:2d} {score1:2d}\n")

    winner = "Player 0" if board.evaluate() > 0 else "Player 1"
    print(f"Game over! Winner: {winner}")
    if num_moves > 0:
        print(f"Average depth per move: {total_depth / num_moves:.3f}")

print(sys.argv)
if len(sys.argv) < 2:
    print("Usage: python play_the_game.py <number of iterations>")
    exit(-1)
iterations = int(sys.argv[1])

if iterations < 1:
    print("invalid number of iterations!")
    exit(-1)

play_game(iterations)
