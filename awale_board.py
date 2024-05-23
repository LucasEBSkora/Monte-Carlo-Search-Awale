class AwaleBoard:
    def __init__(self):
        self.board = [[4] * 6, [4] * 6]
        self.current_player = 0
        self.player_store = [0, 0]

    def get_moves(self):
        return [i for i in range(6) if self.board[self.current_player][i] > 0]

    def get_score(self):
        return self.player_store
    
    def make_move(self, move):
        assert isinstance(move, int), "Move must be an integer"
        seeds = self.board[self.current_player][move]
        self.board[self.current_player][move] = 0
        index = move
        player = self.current_player

        while seeds > 0:
            index = (index + 1) % 6
            if index == 0:
                player = 1 - player
            self.board[player][index] += 1
            seeds -= 1

        if player != self.current_player and 1 <= self.board[player][index] <= 2:
            captured_seeds = self.board[player][index]
            self.board[player][index] = 0
            self.player_store[self.current_player] += captured_seeds

        self.current_player = 1 - self.current_player

    def evaluate(self):
        if self.is_game_over():
            score0 = self.player_store[0] + sum(self.board[0])
            score1 = self.player_store[1] + sum(self.board[1])
            return score0 - score1
        return self.player_store[0] - self.player_store[1]


    def is_game_over(self):
        return all(seeds == 0 for seeds in self.board[0]) or all(seeds == 0 for seeds in self.board[1])

    def copy(self):
        new_board = AwaleBoard()
        new_board.board = [row[:] for row in self.board]
        new_board.current_player = self.current_player
        return new_board
