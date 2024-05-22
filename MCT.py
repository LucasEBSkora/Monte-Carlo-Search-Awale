import random
import math

class MCTSNode:
    def __init__(self, board, move=None, parent=None):
        self.board = board
        self.move = move
        self.parent = parent
        self.children = []
        self.visits = 0
        self.wins = 0
        self.depth = parent.depth + 1 if parent else 0

    def select_child(self):
        return max(self.children, key=lambda node: node.wins / (node.visits + 1e-10) + math.sqrt(2 * math.log(self.visits + 1e-10) / (node.visits + 1e-10)))

    def expand(self):
        moves = self.board.get_moves()
        for move in moves:
            new_board = self.board.copy()
            new_board.make_move(move)
            self.children.append(MCTSNode(new_board, move, self))

    def simulate(self):
        current_board = self.board.copy()
        while not current_board.is_game_over():
            possible_moves = current_board.get_moves()
            if not possible_moves:
                break
            move = random.choice(possible_moves)
            current_board.make_move(move)
        return current_board.evaluate()

    def backpropagate(self, result):
        self.visits += 1
        self.wins += result
        if self.parent:
            self.parent.backpropagate(result)

def mcts_search(board, iterations):
    root = MCTSNode(board)
    max_depth = 0
    for _ in range(iterations):
        node = root
        while node.children:
            node = node.select_child()
        if not node.board.is_game_over():
            node.expand()
        result = node.simulate()
        node.backpropagate(result)
        max_depth = max(max_depth, node.depth)

    best_move = max(root.children, key=lambda node: node.visits).move
    average_depth = max_depth / root.visits if root.visits else 0
    move_evaluations = [child.wins / child.visits if child.visits else 0 for child in root.children]
    return best_move, average_depth, move_evaluations
