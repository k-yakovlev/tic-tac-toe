LOGO = """
,--------.,--.               ,--.                         ,--.                 
'--.  .--'`--' ,---.,-----.,-'  '-. ,--,--. ,---.,-----.,-'  '-. ,---.  ,---.  
   |  |   ,--.| .--''-----''-.  .-'' ,-.  || .--''-----''-.  .-'| .-. || .-. : 
   |  |   |  |\ `--.         |  |  \ '-'  |\ `--.         |  |  ' '-' '\  ---. 
   `--'   `--' `---'         `--'   `--`--' `---'         `--'   `---'  `----' 

"""


def user_want_play(again=False):
    """Return True if user want to play, otherwise return False.

    If user input is incorrect, then extended question will be shown
    again till to correct answer (y/n).
    """
    if not again:
        answer = input('Wanna play? (y/n): ')
    else:
        answer = input('Enter "y" (as "yes") to play or "n" (as "no") to leave the game: ')

    if answer.lower() == 'y':
        return True
    elif answer.lower() == 'n':
        return False
    else:
        return user_want_play(again=True)


def create_players():
    global players, scores
    players = [None, 'X', 'O']
    scores = {'X': 0, 'O': 0}
    return


def create_board():
    """Create new board for game and help-board with cells numbers"""
    global nums, cells
    nums = {'1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9'}
    cells = {'1': '', '2': '', '3': '', '4': '', '5': '', '6': '', '7': '', '8': '', '9': ''}
    return


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

    return


def ask_a_move():
    global player_input
    player_input = input(f'{"":>28s}Enter the cell number: ')
    return


def cell_is_available():
    if player_input in nums.values():
        return True
    return False


def show_error():
    if player_input in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        taken_cell_message = f'Cell "{player_input}" is already taken. Try again.'
        print(f'{taken_cell_message:^78s}')
    else:
        wrong_cell_message = f'It is not a number of cell. Try again.'
        print(f'{wrong_cell_message:^78s}')
    return


def mark_a_cell():
    cells[player_input] = players[player]
    nums[player_input] = ' '
    return


def change_player():
    global player
    player = -player
    return


def row_of_3_marks():
    pass


def check_if_1000_wins():
    if 1000 in scores.values():
        print('1000 Game Over')
    return


def game():
    print(LOGO)
    if user_want_play():
        create_players()
        create_board()
        show_board()
        ask_a_move()
        while not cell_is_available():
            show_board()
            show_error()
            ask_a_move()
        mark_a_cell()


players = []
player = 1
scores = {}
player_input = False
nums = {}
cells = {}
winning_cells = [
    (1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7),
    (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)
]

if __name__ == '__main__':
    game()
