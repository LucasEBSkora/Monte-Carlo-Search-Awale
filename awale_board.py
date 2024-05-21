class AwaleBoard:
    def __init__(self):
        # Initialize the board with 2 rows and 6 columns, each containing 4 seeds
        self.board = [[4] * 6, [4] * 6]
        self.current_player = 0  # Player 0 starts
        self.player_store = [0, 0]  # Initialize a store for each player

    def get_moves(self):
        # Return a list of valid moves for the current player
        return [i for i in range(6) if self.board[self.current_player][i] > 0]
    def get_score(self):
        # Return the current score for each player
        return self.player_store
    
    def make_move(self, move):
        # Ensure that the move argument is an integer
        assert isinstance(move, int), "Move must be an integer"
        seeds = self.board[self.current_player][move]
        self.board[self.current_player][move] = 0
        index = move
        player = self.current_player

        while seeds > 0:
            index = (index + 1) % 6
            if index == 0:
                player = 1 - player  # Switch sides
            self.board[player][index] += 1
            seeds -= 1

        # Check for captures
        if player != self.current_player and 1 <= self.board[player][index] <= 2:
            captured_seeds = self.board[player][index]
            self.board[player][index] = 0
            self.player_store[self.current_player] += captured_seeds  # Add to the player's store

        self.current_player = 1 - self.current_player  # Switch players

    def evaluate(self):
        # Evaluate the board state to determine the winner
        return self.player_store[0] - self.player_store[1]

    def is_game_over(self):
        # Check if the game is over
        return all(seeds == 0 for seeds in self.board[self.current_player])

    def copy(self):
        # Create a deep copy of the board for simulation purposes
        new_board = AwaleBoard()
        new_board.board = [row[:] for row in self.board]
        new_board.current_player = self.current_player
        return new_board