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


def print_board():
    """
    Prints the current state of the gameboard
    """
    print '\n'
    print '\n-+-+-\n'.join('|'.join(curr_board[x:x+3]) for x in (0,3,6))
    print '\n'


def check_winner():
    """
    Returns the (winner, indices of winning squares) if there is one.
    Returns (None, None) if there is no winner yet
    """
    for win in win_indices:
        b = curr_board[win[0]]
        if b in 'XO' and all (curr_board[i] == b for i in win):
            return b, [i+1 for i in win]
    return None, None


def draw():
    """
    Returns whether or not the game is at a draw.
    """
    return all (b in 'XO' for b in curr_board)


def get_open_spaces():
    """
    Returns the number-chars representing empty/available
    squares on the gameboard.
    """
    return [b for b in curr_board if b not in 'XO']


def computer_turn_do(xo):
    """
    Performs a random move.
    Replace this with minimax AI decision.
    """
    options = get_open_spaces()
    choice = random.choice(options)
    curr_board[int(choice)-1] = xo
    return choice


def player_turn_do(xo):
    """
    Prompts user for a position to enter their letter.
    Modifies the gameboard.
    """
    options = get_open_spaces()
    invalid = True
    while invalid:
        choice = raw_input('Put your %s in any of these positions: %s '
                       % (xo, ''.join(options))).strip()
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
    choice = computer_turn_do(xo)
    print 'The computer placed an %s at %s' % (computer, choice)
    return check_winner()


def player_turn(xo):
    """
    Wrapper for player's turn.
    Prints the gameboard before the turn, describes
    the move after it's made.
    """
    print_board()
    choice = player_turn_do(xo)
    print 'You placed an %s at %s' % (player, choice)
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
    print '\nA draw'
