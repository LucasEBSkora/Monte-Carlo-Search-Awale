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
        if self.visits == 0:
            return  self.children[0]
        return max(self.children, key=lambda node: node.wins / (node.visits + 1e-10) + math.sqrt(2 * math.log(self.visits + 1e-10) / (node.visits + 1e-10)))

    def expand(self):
        moves = self.board.get_moves()
        for move in moves:
            new_board = self.board.copy()
            new_board.make_move(move)
            self.children.append(MCTSNode(new_board, move, self))

    def simulate(self):
        current_board = self.board.copy()
        depth = 0
        while not current_board.is_game_over() or depth > 150:
            possible_moves = current_board.get_moves()
            if not possible_moves:
                break
            move = random.choice(possible_moves)
            current_board.make_move(move)
            depth += 1
        score = 0
        if current_board.is_game_over():
            score = 1 if current_board.evaluate() > 0 else -1
        return (score, depth)

    def backpropagate(self, result):
        self.visits += 1
        self.wins += result
        if self.parent:
            self.parent.backpropagate(result)

def mcts_search(board, iterations):
    root = MCTSNode(board)
    sum_depth = 0
    for _ in range(iterations):
        node = root
        sel_depth = 0
        while node.children:
            node = node.select_child()
            sel_depth += 1
        if node.visits > 0:
            node.expand()
        result, sim_depth = node.simulate()
        
        node.backpropagate(result)
        # the depth of the path is the number of moves we had to select + the number of moves done in the simulation
        sum_depth += sel_depth + sim_depth 

    best_move = max(root.children, key=lambda node: node.wins).move
    average_depth = sum_depth / iterations
    move_evaluations = [child.wins for child in root.children]
    return best_move, average_depth, move_evaluations
