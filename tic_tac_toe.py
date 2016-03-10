import random


# list of characters, keeps track of Xs and Os held in format:
# 1 2 3
# 4 5 6
# 7 8 9
curr_board = list('123456789')

# tuples for winning indices of curr_board
# i.e. when these indices hold the same letter, there is a winner
win_indices = ((0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6))

# Global variable for computer's choice
computer_choice = None


def print_board():
    """
    Prints the current state of the gameboard
    """
    print '\n'
    print '\n-+-+-\n'.join('|'.join(curr_board[x:x+3]) for x in (0,3,6))
    print '\n'


def check_winner(board=curr_board):
    """
    Returns the (winner, indices of winning squares) if there is one.
    Returns (None, None) if there is no winner yet
    """
    for win in win_indices:
        b = board[win[0]]
        if b in 'XO' and all (board[i] == b for i in win):
            return b, [i+1 for i in win]
    return None, None


def draw(board=curr_board):
    """
    Returns whether or not the game is at a draw.
    """
    return all (b in 'XO' for b in board)


def get_open_spaces(board=curr_board):
    """
    Returns the number-chars representing empty/available
    squares on the gameboard.
    """
    return [b for b in board if b not in 'XO']


def game_over(board):
    """
    Checks whether or not the game has ended in some way.
    """
    return check_winner(board=board)[0] or draw(board=board)


def get_possible_boards(board, moves, player):
    """
    Returns a list of possible board layouts, given the player
    whose turn it is, and a list of valid moves.
    """
    boards = []
    for move in moves:
        new_board = board[:]
        new_board[int(move)-1] = player
        boards.append(new_board)
    return boards


def minimax_score(board):
    """
    Evaluation function that assigns a score to some ending board
    layout.
    """
    winner = check_winner(board=board)
    if winner[0]:
        if winner[0] == computer:
            return 10
        else:
            return -10
    else:
        return 0

def minimax(board, curr_player, other_player):
    """
    Calculates the best move for the computer, based on building
    a tree of all possible ways the remainder of the game can go.
    Chooses the options with the best outcome, i.e. where the
    computer has the lowest chance to lose.
    """
    global computer_choice
    if game_over(board):
        return minimax_score(board)
    scores = []
    moves = get_open_spaces(board=board)
    new_boards = get_possible_boards(board, moves, curr_player)
    for boards in new_boards:
        scores.append(minimax(boards, other_player, curr_player))
    if curr_player == computer:
        max_index = scores.index(max(scores))
        computer_choice = moves[max_index]
        return scores[max_index]
    else:
        min_index = scores.index(min(scores))
        computer_choice = moves[min_index]
        return scores[min_index]


def player_turn_do(xo):
    """
    Prompts user for a position to enter their letter.
    Modifies the gameboard.
    """
    options = get_open_spaces()
    invalid = True
    while invalid:
        choice = raw_input('Put your %s in any of these positions - %s: '
                       % (xo, ', '.join(options))).strip()
        if choice in options:
            invalid = False
        else:
            print 'Invalid choice! Try again.'
    curr_board[int(choice)-1] = xo
    return choice


def computer_turn(xo):
    """
    Wrapper for computer's turn.
    Prints the gameboard before the turn, describes
    the move after it's made.
    """
    print_board()
    global minimax_depth
    minimax_depth = 0
    turn_score = minimax(curr_board, computer, player)
    choice = computer_choice
    curr_board[int(choice)-1] = computer
    print 'The computer placed an %s at cell %s' % (computer, choice)
    return check_winner()


def player_turn(xo):
    """
    Wrapper for player's turn.
    Prints the gameboard before the turn, describes
    the move after it's made.
    """
    print_board()
    choice = player_turn_do(xo)
    print 'You placed an %s at cell %s' % (player, choice)
    return check_winner()


# Assigning the player and computer their letters
invalid_letter = True
while invalid_letter:
    player = raw_input('Would you like to play as X or O? ').strip()
    if player in 'XO':
        invalid_letter = False
    else:
        print 'Invalid letter.'
if player == 'O':
    computer = 'X'
else:
    computer = 'O'




# Gameplay loop
# Keeps taking turns until one of the turns
# returns a non-None value, meaning the game has been won.
while not draw():
    s = computer_turn(computer)
    if s[0]:
        print_board()
        print '\nWinner: %s\nCells: %s' % s
        break
    if not draw():
        s = player_turn(player)
        if s[0]:
            print_board()
            print '\nWinner: %s\nCells: %s' % s
            break
else:
    print '\nYou tied. Better than losing...'
