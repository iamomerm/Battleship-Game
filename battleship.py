import random

def create_board(size):
    board = []
    for i in range(size):
        board.append(['X' for j in range(size)])
    return board

def print_board(board, size):
    print('[Gamebot] ' + 'Board:\n')
    prnt = '     '
    for i in range(size):
        prnt += str(i) + ' '
    print(prnt + '\n')
    for i in range(size):
        prnt = str(i) + '    '
        for j in range(size):
            prnt += board[i][j] + ' '
        print(prnt)
    print()

def player_move(board, battleships):
    column = valid_input('[Gamebot] Enter Column (0 - %d)' % (board_size - 1), range(board_size), cast_value_to_int=True)
    row = valid_input('[Gamebot] Enter Row (0 - %d)' % (board_size - 1), range(board_size), cast_value_to_int=True)
    return pin(board, battleships, column, row)

def pin(board, battleships, column, row):
    if [row,column] in battleships:
        battleships.remove([row,column])
        board[row][column] = 'O'
        print('[Gamebot] You Have Destroyed a Battleship Well Done! (Battleships: %d/3)' % len(battleships))
    else:
        board[row][column] = '#'
        print('[Gamebot] You Missed!')
    return board, battleships

def valid_input(prompt, valid_values, cast_value_to_int=False):
    while True:
        value = input(prompt + ' (Type "EXIT" to Exit): ')
        if value.upper() == 'EXIT':
            print('[Gamebot] Exiting...')
            exit()
        elif cast_value_to_int:
            try:
                value = int(value)
            except:
                print('[Gamebot] Invalid Input Type - Expected an Integer (!)')
        if value not in valid_values:
            print('[Gamebot] Invalid Value (!)')
        else:
            return value

if __name__ == '__main__':
    # Pre-Game
    moves = 0
    
    # Game
    print('Welcome to BATTLEHIP!\n')
    board_size = valid_input('[Gamebot] Enter Board Size (2 - 10)', range(2,11), cast_value_to_int=True)
    board = create_board(board_size)
    battleships = random.sample([[i,j] for i in range(board_size) for j in range(board_size)], 3)
    print('[Gamebot] 3 Battleships Scattered Across the Board, Good Luck!')
    while battleships:
        print_board(board, board_size)
        board, battleships = player_move(board, battleships)
        moves += 1
        if not battleships:
            print('[Gamebot] You Destroyed all the Battleships, Well Done! (Moves: %d)' % moves)
            break
