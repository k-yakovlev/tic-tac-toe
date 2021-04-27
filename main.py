LOGO = """
,--------.,--.               ,--.                         ,--.                 
'--.  .--'`--' ,---.,-----.,-'  '-. ,--,--. ,---.,-----.,-'  '-. ,---.  ,---.  
   |  |   ,--.| .--''-----''-.  .-'' ,-.  || .--''-----''-.  .-'| .-. || .-. : 
   |  |   |  |\ `--.         |  |  \ '-'  |\ `--.         |  |  ' '-' '\  ---. 
   `--'   `--' `---'         `--'   `--`--' `---'         `--'   `---'  `----' 

"""


def ask_new_game(attempt):
    """Ask user to play a game of tic-tac-toe."""
    if attempt == 1:
        answer = input('Wanna play? (y/n): ')
    else:
        answer = input('Enter "y" (as "yes") to play or "n" (as "no") to leave the game: ')

    if answer.lower() == 'y':
        return create_players()
    elif answer.lower() == 'n':
        return
    return ask_new_game(attempt=2)


def create_players():
    global players, scores
    players = [None, 'X', 'O']
    scores = {'X': 0, 'O': 0}
    return create_board()


def create_board():
    """Create new board for game and help-board with cells numbers"""
    global nums, cells
    nums = {'1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9'}
    cells = {'1': '', '2': '', '3': '', '4': '', '5': '', '6': '', '7': '', '8': '', '9': ''}
    return show_board()


def show_board():
    help_1 = f'{nums["1"]:^5s}│{nums["2"]:^5s}│{nums["3"]:^5s}'
    help_2 = f'{nums["4"]:^5s}│{nums["5"]:^5s}│{nums["6"]:^5s}'
    help_3 = f'{nums["7"]:^5s}│{nums["8"]:^5s}│{nums["9"]:^5s}'

    board_1 = f'{cells["1"]:^5s}│{cells["2"]:^5s}│{cells["3"]:^5s}'
    board_2 = f'{cells["4"]:^5s}│{cells["5"]:^5s}│{cells["6"]:^5s}'
    board_3 = f'{cells["7"]:^5s}│{cells["8"]:^5s}│{cells["9"]:^5s}'

    line = '─────┼─────┼─────'
    score_board = f'"X"{scores["X"]:>4d} : {scores["O"]:<4d}"O"'
    current_player = f'Player "{players[player]}"'

    print('\n' * 100)
    print(LOGO)
    print(f'{help_1:>20s}{"Game Score":^38s}{board_1:<20s}')
    print(f'{line:>20s}{score_board:^38s}{line:<20s}')
    print(f'{help_2:>20s}{"":^38s}{board_2:<20s}')
    print(f'{line:>20s}{"":^38s}{line:<20s}')
    print(f'{help_3:>20s}{current_player:^38s}{board_3:<20s}')

    return ask_next_move()


def ask_next_move():
    global player_input
    if player_input and cell_unavailable():
        if player_input in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            taken_cell_message = f'Cell "{player_input}" is already taken. Try again.'
            print(f'{taken_cell_message:^78s}')
        else:
            wrong_cell_message = f'It is not a number of cell. Try again.'
            print(f'{wrong_cell_message:^78s}')
    player_input = input(f'{"":>28s}Enter the cell number: ')
    return cell_unavailable()


def cell_unavailable():
    if player_input in nums.values():
        mark_a_cell()
        return False
    return True


def mark_a_cell():
    cells[player_input] = players[player]
    nums[player_input] = ' '


def change_player():
    global player
    player = -player


def check_if_1000_wins():
    if 1000 in scores.values():
        print('1000 Game Over')
    return


def game():
    print(LOGO)
    ask_new_game(attempt=1)


players = []
player = 1
scores = {}
player_input = False
nums = {}
cells = {}

if __name__ == '__main__':
    game()
