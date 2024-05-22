from awale_board import *
from MCT import *

def play_game(iterations):
    board = AwaleBoard()
    total_depth = 0
    num_moves = 0

    while not board.is_game_over():
        if board.current_player == 0:
            print("Player 0's turn")
            move, avg_depth, move_evaluations = mcts_search(board, iterations)
            total_depth += avg_depth
            num_moves += 1
            print(f"Average search depth: {avg_depth:.3f}")
            print(f"Move evaluations: {move_evaluations}")
        else:
            print("Player 1's turn")
            move = random.choice(board.get_moves())

        board.make_move(move)
        print(f"Board state: {board.board}")
        score0, score1 = board.get_score()
        print(f"Score: Player 0 - {score0}, Player 1 - {score1}")

    winner = "Player 0" if board.evaluate() > 0 else "Player 1"
    print(f"Game over! Winner: {winner}")
    if num_moves > 0:
        print(f"Average depth per move: {total_depth / num_moves:.3f}")

play_game(10) 

