from IPython.display import clear_output
import random

def display_board(board):
    print(f'{board[7]} | {board[8]} | {board[9]}')
    print(f'{board[4]} | {board[5]} | {board[6]}')
    print(f'{board[1]} | {board[2]} | {board[3]}')

game_board = ['Ignore',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']

def player_input():
    marker = ''

    while marker not in ['X','O']:
        marker = input("Player 1, pick a marker 'X' or 'O': ").upper()

        if marker not in ['X', 'O']:    
            print('Invalid choice!')

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, marker):

    if ((board[7] == board[8] == board[9] == marker) or 
        (board[4] == board[5] == board[6] == marker) or 
        (board[1] == board[2] == board[3] == marker) or 
        (board[7] == board[4] == board[1] == marker) or 
        (board[8] == board[5] == board[2] == marker) or 
        (board[9] == board[6] == board[3] == marker) or 
        (board[7] == board[5] == board[3] == marker) or 
        (board[9] == board[5] == board[1] == marker)):
        
        return True
    else:
        return False

def choose_first():

    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'
    
def space_check(board, position):

    return board[position] == ' '

def full_board_check(board):
    for item in range(1,10):
        if space_check(board,item):
            return False
    return True

def player_choice(board):
    position = 0

    while position not in range(1,10) or not space_check(board,position):
        position = int(input('Choose a position (1-9): '))
        
        if position not in range(1,10):
            print("That's not between 1 and 9!")
        elif not space_check(board, position):
            print("That spot is already taken! Try again.")

    return position
    
def replay():
    validation = ' '

    while validation not in ['Y', 'N']:
        validation = input('Do yo want to keep on playing? (Y or N): ').upper()

        if validation not in ['Y', 'N']:
            print('That is not an Y or a N')
        
    return validation == 'Y'

print('Welcome to Tic Tac Toe!')
    
while True:
    game_board = [' '] * 10
    p1_marker, p2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first!')
    
    game_on = True
    
    while game_on:
        display_board(game_board)

        if turn == 'Player 1':
            marker = p1_marker
        else:
            marker = p2_marker

        print(f"{turn}'s turn ({marker})")
        position = player_choice(game_board)
        place_marker(game_board, marker, position)

        if win_check(game_board, marker):
            display_board(game_board)
            print(f'Congratulations! {turn} has won the game!')
            game_on = False
        elif full_board_check(game_board):
            display_board(game_board)
            print("It's a draw!")
            game_on = False
        else:
            if turn == 'Player 1':
                turn = 'Player 2'
            else:
                turn = 'Player 1'

    if not replay():
        print("Thanks for playing!")
        break