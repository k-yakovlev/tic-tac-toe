import random

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
        words = ['Enter', 'Type', 'Only', 'Just', 'WARNING:']
        word = random.choice(words)
        answer = input(f'{word} "y" (as "yes") to play or "n" (as "no") to leave the game: ')

    if answer.lower() == 'y':
        return create_players()
    elif answer.lower() == 'n':
        return
    ask_new_game(attempt=2)


def create_players():
    global players, scores
    players = [None, 'X', 'O']
    scores = {'X': 0, 'O': 0}
    return create_boards()


def create_boards():
    """Create new board for game and help-board with cells numbers"""
    global nums, cells
    nums = {'1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9'}
    cells = {'1': '', '2': '', '3': '', '4': '', '5': '', '6': '', '7': '', '8': '', '9': ''}
    return show_board()


def show_board():
    global nums, cells
    i = 1
    wrong_cell = False
    player_input = ''
    # TODO: Fix while loop. Current loop doesn't process the last cell.
    while '' in cells.values():
        help_1 = f'{nums["1"]:^5s}│{nums["2"]:^5s}│{nums["3"]:^5s}'
        help_2 = f'{nums["4"]:^5s}│{nums["5"]:^5s}│{nums["6"]:^5s}'
        help_3 = f'{nums["7"]:^5s}│{nums["8"]:^5s}│{nums["9"]:^5s}'

        board_1 = f'{cells["1"]:^5s}│{cells["2"]:^5s}│{cells["3"]:^5s}'
        board_2 = f'{cells["4"]:^5s}│{cells["5"]:^5s}│{cells["6"]:^5s}'
        board_3 = f'{cells["7"]:^5s}│{cells["8"]:^5s}│{cells["9"]:^5s}'

        line = '─────┼─────┼─────'
        score_board = '"X"' + f'{scores["X"]:>4d}' + ' : ' + f'{scores["O"]:<4d}' + '"O"'
        current_player = f'Player "{players[i]}"'

        print('\n' * 100)
        print(LOGO)
        print(f'{help_1:>20s}{"Game Score":^38s}{board_1:<20s}')
        print(f'{line:>20s}{score_board:^38s}{line:<20s}')
        print(f'{help_2:>20s}{"":^38s}{board_2:<20s}')
        print(f'{line:>20s}{"":^38s}{line:<20s}')
        print(f'{help_3:>20s}{current_player:^38s}{board_3:<20s}')
        if wrong_cell:
            if player_input in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                taken_cell_message = f'Cell "{player_input}" is already taken. Try again.'
                print(f'{taken_cell_message:^78s}')
            elif len(player_input) > 43:
                long_input_message = f'The input is too long. Try again.'
                print(f'{long_input_message:^78s}')
            else:
                wrong_cell_message = f'"{player_input}" is not a cell number. Try again.'
                print(f'{wrong_cell_message:^78s}')
        player_input = input(f'{"":>28s}Enter the cell number: ')

        if player_input in nums.values():
            cells[player_input] = players[i]
            nums[player_input] = ' '
            i = -i
            wrong_cell = False
        else:
            wrong_cell = True

        if 1000 in scores.values():
            print('1000 Game Over')
            return

    return


players = []
scores = {}

nums = {}
cells = {}


if __name__ == '__main__':
    print(LOGO)
    ask_new_game(attempt=1)
