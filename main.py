import os
import time

# import os & os.system('') added for correct work in windows cmd.
os.system('')

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
    if current_round > 0:
        answer = input(f'{"":28s}Another round? (y/n): ')
    else:
        print(LOGO)
        if not again:
            answer = input(f'{"Wanna play? (y/n): ":>49s}')
        else:
            answer = input(f'{"":6s}Enter "y" (as "yes") for start the game or "n" (as "no") for exit: ')

    if answer.lower() == 'y':
        return True
    elif answer.lower() == 'n':
        return False
    else:
        return user_want_play(again=True)


def new_game():
    global player, current_round, scores
    player = 'O'
    current_round = 1
    scores = {'X': 0, 'O': 0}
    return


def create_board():
    """Create new board for game and help-board with cells numbers"""
    global nums, cells, players_cells, current_round
    nums = {'1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9'}
    cells = {'1': '', '2': '', '3': '', '4': '', '5': '', '6': '', '7': '', '8': '', '9': ''}
    players_cells = {'X': set(), 'O': set()}
    current_round += 1
    return


def show_board(result=None):
    help_1 = f'│{nums["1"]:^5s}│{nums["2"]:^5s}│{nums["3"]:^5s}│'
    help_2 = f'│{nums["4"]:^5s}│{nums["5"]:^5s}│{nums["6"]:^5s}│'
    help_3 = f'│{nums["7"]:^5s}│{nums["8"]:^5s}│{nums["9"]:^5s}│'

    board_1 = f'│{cells["1"]:^5s}│{cells["2"]:^5s}│{cells["3"]:^5s}│'
    board_2 = f'│{cells["4"]:^5s}│{cells["5"]:^5s}│{cells["6"]:^5s}│'
    board_3 = f'│{cells["7"]:^5s}│{cells["8"]:^5s}│{cells["9"]:^5s}│'

    header_line = '┌─────┬─────┬─────┐'
    middle_line = '├─────┼─────┼─────┤'
    footer_line = '└─────┴─────┴─────┘'

    score_board = f'"X"{scores["X"]:>4d} : {scores["O"]:<4d}"O"'
    player_string = f'Player "{player}"'
    round_string = f'Round {current_round}'

    print(LOGO)
    print(f'{header_line:>20s}{"Game Score":^38s}{header_line:<20s}')
    print(f'{help_1:>20s}{score_board:^38s}{board_1:<20s}')
    print(f'{middle_line:>20s}{"":^38s}{middle_line:<20s}')
    print(f'{help_2:>20s}{round_string:^38s}{board_2:<20s}')
    print(f'{middle_line:>20s}{"":^38s}{middle_line:<20s}')
    print(f'{help_3:>20s}{"":^38s}{board_3:<20s}')
    print(f'{footer_line:>20s}{player_string:^38s}{footer_line:<20s}')
    print()
    if result:
        if result == 'win':
            message = f'Player "{player}" wins the round!'
            highlight = green_highlight
        else:
            message = 'It\'s a draw - nobody wins.'
            highlight = yellow_highlight
        print(f'{highlight}{message:^78s}{end_highlight}')
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
        error_message = f'Cell "{player_input}" is already taken.'
    else:
        error_message = f'It is not a number of cell.'
    print(f'{red_highlight}{error_message:^78s}{end_highlight}')
    return


def save_a_move():
    cells[player_input] = player
    nums[player_input] = ' '
    players_cells[player].add(int(player_input))
    return


def is_row_of_3_marks():
    global winning_rows
    winning_rows = [_ for _ in winning_cells if _.issubset(players_cells[player])]
    if winning_rows:
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


def highlight_winning_rows():
    for row in winning_rows:
        for cell in row:
            cells[str(cell)] = f'{green_blink_highlight}{cells[str(cell)]:^5s}{end_highlight}'
    return


def update_score():
    scores[player] += 1
    return


def is_1000_score():
    if 1000 in scores.values():
        print()
        print(f'{"Wow, 1000 scores! Take a rest.":^78s}')
        print(f'{"GAME OVER":^78s}')
        for _ in range(10, -1, -1):
            timer = f'{_:^78}'
            print(timer, end='\r')
            time.sleep(1)
        return True
    else:
        return False


def clear_screen():
    print("\033[H\033[2J", end="", flush=True)
    return


def get_next_move(error=False):
    clear_screen()
    show_board()
    if error:
        show_error()
    ask_a_move()


# TODO: add prompt & actions for quit anytime & reset score
# TODO: refactor game() and join show_error() to show_board()
# TODO: fix "it is" to "it's" in error message
# TODO: get_error() before show_board() if it need
# TODO: add docstrings.
# TODO: clear screen if error on welcome screen
# TODO: clear screen if error when ask another round


def game():
    clear_screen()
    while not is_1000_score() and user_want_play():
        create_board()
        while not is_row_of_3_marks() and not is_all_cells_filled():
            change_player()
            get_next_move()
            while not cell_is_available():
                get_next_move(error=True)
            save_a_move()
        clear_screen()
        if is_row_of_3_marks():
            highlight_winning_rows()
            update_score()
            show_board(result='win')
        else:
            show_board(result='draw')
    else:
        clear_screen()


player = 'O'
current_round = 0
scores = {'X': 0, 'O': 0}
players_cells = {}
player_input = False
nums = {}
cells = {}
winning_cells = [
    {1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {1, 4, 7},
    {2, 5, 8}, {3, 6, 9}, {1, 5, 9}, {3, 5, 7}
]
winning_rows = []

red_highlight = '\033[91;1m'
green_highlight = '\033[92;1m'
green_blink_highlight = '\033[92;5m'
yellow_highlight = '\033[93;1m'
end_highlight = '\033[0m'

if __name__ == '__main__':
    game()
