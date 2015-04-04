# Import randint(low, high) function from the random module
from random import randint 

board = []

# Create a 5x5 grid of Os
for lst in range(5):
    board.append(["O"] * 5)

# Function to print board in a Grid
def print_board(board):
    for row in range(5):
        print " ".join(board[row])

# Function that returns a random row and column index
def random_row(board):
    random_row = randint(0, len(board) - 1)
    return random_row

def random_col(board):
    random_col = randint(0, len(board) - 1)
    return random_col

ship_row = random_row(board)
ship_col = random_col(board)

#print ship_row
#print ship_col

# 4 tries to guess correctly
for turn in range(4):
    # Allow user to guess location
    guess_row = int(raw_input("Guess Row: "))
    guess_col = int(raw_input("Guess Col: "))

    # You sunk my battleship, You missed, Out of range, You LOSE
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sank my battleship!"
        break
    # They guess it wrong
    else:
        # Not in the grid
        if guess_row not in range(5) or \
        guess_col not in range(5):
            print "Oops, that's not even in the ocean."
        # Already Guessed
        elif board[guess_row][guess_col] == 'X':
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
        # Game over
        if turn == 3:
            print "Game Over"
    # Print which turn they are at        
    print "Turn", turn + 1    
    print_board(board)