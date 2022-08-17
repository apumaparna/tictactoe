"""
Tic Tac Toe Player
"""

import math
import copy

# Define variables
X = "X"
O = "O"
EMPTY = None

# Initial state - board is fully empty
def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


# In the initial game, X gets the first move. 
# Then, you alternate between players. 
# Want to find out who has the next move. 
def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = 0 
    o_count = 0

    for i in range(len(board)): 
        for j in range(len(board[i])): 
            if board[i][j] == "X": 
                x_count = x_count + 1
            elif board[i][j] == "O": 
                o_count = o_count + 1 
    
    if x_count > o_count: 
        return "O" 
    elif o_count > x_count: 
        return "X"
    # o_count = x_count 
    # This can only happen with a starting board. 
    # X goes first. 
    else: 
        return "X"

# i corresponds to the row of the move (0, 1, or 2) 
# j corresponds to which cell in the row corresponds to the move (also 0, 1, or 2)
# Possible moves are any cells on the board that do not already have an X or an O in them.
# Any return value is acceptable if a terminal board is provided as input.
def actions(board):
    
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = [] 

    if terminal(board) == True: 
        for i in range(len(board)): 
            for j in range(len(board[i])): 
                if board[i][j] == EMPTY: 
                    actions.append((i, j)) 
        
    return actions



# Does not modify the original board, returns a separate board 
# If action is not a valid action for the board, your program should raise an exception.
# The board you return is the board that results from applying the action by whomever is the player. 
# You’ll likely want to make a deep copy of the board first before making any changes.
def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Make a deep copy of the original board 
    new_board = copy.deepcopy(board)
    
    # Check who the player is 
    current_player = player(board)

    (i, j) = action
    new_board[i][j] = current_player

    return new_board



# If the X player has won the game, your function should return X. 
# If the O player has won the game, your function should return O.
# If there is no winner of the game (either because the game is in progress, or because it ended in a tie), the function should return None.
def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError

# Game can be over because someone won or all the cells are filled up without a winner 
# Otherwise the game is still in progress. 
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError

# Accepts only terminal board 
def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError

# The move returned should be the optimal action (i, j) that is one of the allowable actions on the board
# If multiple moves are equally optimal, any of those moves is acceptable.
# If the board is a terminal board, the minimax function should return None.
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
