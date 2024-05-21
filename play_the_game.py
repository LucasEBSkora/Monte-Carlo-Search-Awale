from awale_board import *
from MCT import *

def play_game():
    board = AwaleBoard()
    while not board.is_game_over():
        if board.current_player == 0:
            print("Player 0's turn")
            move = mcts_search(board, 1000)  # Use 1000 iterations for MCTS
        else:
            print("Player 1's turn")
            move = random.choice(board.get_moves())
        board.make_move(move)
        print(board.board)
        score0, score1 = board.get_score()  # Get the scores
        print(f"Score: Player 0 - {score0}, Player 1 - {score1}")  # Print the scores
    winner = "Player 0" if board.evaluate() > 0 else "Player 1"
    print(f"Game over! Winner: {winner}")

play_game()