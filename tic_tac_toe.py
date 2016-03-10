import random

curr_board = list('123456789')
win_indices = ((0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6))

def print_board():
    print('\n-+-+-\n'.join('|'.join(curr_board[x:x+3]) for x in (0,3,6)))

def score():
    for win in win_indices:
        b = curr_board[win[0]]
        if b in 'XO' and all (curr_board[i] == b for i in win):
            return b, [i+1 for i in win]
    return None, None

def finished():
    return all (b in 'XO' for b in curr_board)

def space():
    return [b for b in curr_board if b not in 'XO']

def my_turn(xo):
    """
    Performs a random move.
    Replace this with minimax AI decision.
    """
    options = space()
    choice = random.choice(options)
    curr_board[int(choice)-1] = xo
    return choice

def your_turn(xo):
    options = space()
    invalid = True
    while invalid:
        choice = input(" Put your %s in any of these positions: %s "
                       % (xo, ''.join(options))).strip()
        if choice in options:
            invalid = False
        else:
            print("Whoops I don't understand the input")
    curr_board[int(choice)-1] = xo
    return choice

def me(xo):
    print_board()
    print('I go at', my_turn(xo))
    return score()

def you(xo):
    print_board()
    print('You went at', your_turn(xo))
    return score()



invalid_letter = True
while invalid_letter:
    player = input("Would you like to play as X or O? ").strip()
    if player in 'XO':
        invalid_letter = False
    else:
        print "Invalid letter."
if player == 'O':
    computer = 'X'
else:
    computer = 'O'


while not finished():
    s = me()
    if s[0]:
        print_board()
        print "\n%s wins across %s" % s
        break
    if not finished():
        s = you('O')
        if s[0]:
            print_board()
            print "\n%s wins across %s" % s
            break
else:
    print "\nA draw"
