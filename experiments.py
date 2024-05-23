from awale_board import *
from MCT import *
import numpy as np
import matplotlib.pyplot as plt

Ngames = 1000
iterations = 100
victories = 0
scores = {}
scores_array = []
nTurns = {}
nTurns_array = []

def incrementDict(dict, key):
    if key in dict.keys():
        dict[key] += 1
    else:
        dict[key] = 1

def play_game(iterations):
    global victories
    board = AwaleBoard()
    num_moves = 0
    while not board.is_game_over():
        num_moves += 1
        if board.current_player == 0:
            move, avg_depth, move_evaluations = mcts_search(board, iterations)
        else:
            move = random.choice(board.get_moves())

        board.make_move(move)
        score0, score1 = board.get_score()
    
    if board.evaluate() > 0:
        victories+=1
    incrementDict(scores, board.evaluate())
    incrementDict(nTurns, num_moves)
    scores_array.append(board.evaluate())
    nTurns_array.append(num_moves)

for _ in range(Ngames):
  play_game(iterations)

def dictToImage(dict, imageTitle, xLabel, yLabel, path):
    min_val = min(dict.keys())
    max_val = max(dict.keys())
    n_vals = max_val+1 - min_val
    dictAsList = [0]*(n_vals)
    for key in dict.keys():
        dictAsList[key- min_val] = dict[key]
    print(dictAsList)
    plt.bar(range(min_val, max_val+1), dictAsList)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(imageTitle)
    plt.savefig(path)
    plt.cla()


dictToImage(scores, "Histogramme des differences de pontuations finales", "difference entre pontuation du joueur 0 e du joueur 1", "nombre d'occurrences", "pontuations.png")
dictToImage(nTurns, "Histogramme du nombre de tours pour finir le jeu", "nombre de tours", "nombre d'occurrences", "NbTours.png")
print(victories)
print(scores_array)
print(nTurns_array)
print(np.mean(scores_array))
print(np.std(scores_array))
print(np.mean(nTurns_array))
print(np.std(nTurns_array))