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

    def select_child(self):
        # Select a child node based on UCT (Upper Confidence Bound for Trees)
        return max(self.children, key=lambda node: node.wins / (node.visits + 1e-10) + math.sqrt(2 * math.log(self.visits + 1e-10) / (node.visits + 1e-10)))

    def expand(self):
        # Expand the tree by adding a new child node
        moves = self.board.get_moves()
        for move in moves:
            new_board = self.board.copy()
            new_board.make_move(move)
            self.children.append(MCTSNode(new_board, move, self))

    def simulate(self):
        # Perform a random simulation from the current node
        current_board = self.board.copy()
        while not current_board.is_game_over():
            possible_moves = current_board.get_moves()
            if not possible_moves:
                break
            move = random.choice(possible_moves)
            current_board.make_move(move)
        return current_board.evaluate()

    def backpropagate(self, result):
        # Update the node's statistics based on the simulation result
        self.visits += 1
        self.wins += result
        if self.parent:
            self.parent.backpropagate(result)

def mcts_search(board, iterations):
    root = MCTSNode(board)
    for _ in range(iterations):
        node = root
        # Selection
        while node.children:
            node = node.select_child()
        # Expansion
        if not node.board.is_game_over():
            node.expand()
        # Simulation
        result = node.simulate()
        # Backpropagation
        node.backpropagate(result)
    return max(root.children, key=lambda node: node.visits).move