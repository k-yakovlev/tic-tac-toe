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


def new_game():
    global player, current_round, scores
    player = 'X'
    current_round = 1
    scores = {'X': 0, 'O': 0}
    return


def create_board():
    """Create new board for game and help-board with cells numbers"""
    global nums, cells, players_cells
    nums = {'1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9'}
    cells = {'1': '', '2': '', '3': '', '4': '', '5': '', '6': '', '7': '', '8': '', '9': ''}
    players_cells = {'X': set(), 'O': set()}
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
    player_string = f'Player "{player}"'
    round_string = f'Round {current_round}'

    print('\n' * 100)
    print(LOGO)
    print(f'{help_1:>20s}{"Game Score":^38s}{board_1:<20s}')
    print(f'{line:>20s}{score_board:^38s}{line:<20s}')
    print(f'{help_2:>20s}{"":^38s}{board_2:<20s}')
    print(f'{line:>20s}{round_string:^38s}{line:<20s}')
    print(f'{help_3:>20s}{"":^38s}{board_3:<20s}')
    print(f'{player_string:^78s}')

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


def save_a_move():
    cells[player_input] = player
    nums[player_input] = ' '
    players_cells[player].add(int(player_input))
    return


def is_row_of_3_marks():
    global winning_row
    winning_row = [_ for _ in winning_cells if _.issubset(players_cells[player])]
    if winning_row:
        return True
    else:
        return False


def is_all_cells_filled():
    if '' in cells.values():
        return False
    else:
        return True


def change_player():
    global player
    if player == 'X':
        player = 'O'
    else:
        player = 'X'
    return


def highlight_winning_row():
    green_font = '\033[1;32;1m'
    for cell in winning_row:
        cells[str(cell)] = green_font + cells[str(cell)]
    return


def update_score():
    scores[player] += 1
    return


def show_result(win=False):
    if not win:
        message = 'It\'s a draw. Try another round!'
    else:
        message = f'Player "{player}" wins the round!'
    print(f'{message:^78s}')
    return


def is_1000_score():
    if 1000 in scores.values():
        print('Wow, 1000 scores! Take a rest, game over.')
        return True
    else:
        return False


def user_want_new_round():
    answer = input('Another round? (y/n): ')
    if answer.lower() == 'y':
        return True
    elif answer.lower() == 'n':
        return False
    else:
        return user_want_new_round()


def change_round():
    global current_round
    current_round += 1
    return


def quit_game():
    print('See you later!')
    return


def game():
    print(LOGO)
    while user_want_play():
        create_board()
        while not is_row_of_3_marks() or is_all_cells_filled():
            show_board()
            ask_a_move()
            while not cell_is_available():
                show_board()
                show_error()
                ask_a_move()
            save_a_move()
            change_player()
        if is_row_of_3_marks():
            highlight_winning_row()
            update_score()
        show_board()
        show_result()
        if is_1000_score():
            quit_game()
        if user_want_new_round():
            change_round()
    else:
        quit_game()


player = 'X'
current_round = 1
scores = {'X': 0, 'O': 0}
players_cells = {}
player_input = False
nums = {}
cells = {}
winning_cells = [
    {1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {1, 4, 7},
    {2, 5, 8}, {3, 6, 9}, {1, 5, 9}, {3, 5, 7}
]
winning_row = []

if __name__ == '__main__':
    game()
