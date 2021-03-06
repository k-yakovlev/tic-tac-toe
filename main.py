#!/usr/bin/env python3

import os
import sys
import time

# import os & os.system('') added for correct work in windows cmd.
os.system('')

LOGO = (
    '  _______            __                   __            ',
    ' /_  __(_)____      / /_____ ______      / /_____  ___  ',
    '  / / / / ___/_____/ __/ __ `/ ___/_____/ __/ __ \/ _ \ ',
    ' / / / / /__/_____/ /_/ /_/ / /__/_____/ /_/ /_/ /  __/ ',
    '/_/ /_/\___/      \__/\__,_/\___/      \__/\____/\___/  ',
)


def print_logo():
    """Print logo aligned in the center of board."""
    for _ in LOGO:
        print(f'{"":7}{_}')
    print()


def user_want_play(again=None):
    """Return True if user want to play.

    If user input is incorrect, then extended question will be shown.
    """
    if current_round > 0:
        print()
        answer = input(f'{"":23}Another round? (y/n): ')
    else:
        print_logo()
        if not again:
            answer = input(f'{"Wanna play? (y/n): ":>43}')
        else:
            answer = input(f'Enter "y" (as "yes") for start the game'
                           f' or "n" (as "no") for exit: ')

    if answer.lower() == 'y':
        return True
    elif answer.lower() != 'n':
        clear_screen()
        if current_round > 0:
            show_board()
        return user_want_play(again=True)
    return None


def create_board():
    """Create new board for game and help-board with cells numbers"""
    global nums, cells, players_cells, current_round
    nums = {
        '1': '1', '2': '2', '3': '3',
        '4': '4', '5': '5', '6': '6',
        '7': '7', '8': '8', '9': '9',
    }
    cells = {
        '1': '', '2': '', '3': '',
        '4': '', '5': '', '6': '',
        '7': '', '8': '', '9': '',
    }
    players_cells = {'X': set(), 'O': set()}
    current_round += 1


def show_board(result=None):
    """Show board with prompt & playing fields, game data (score, round, etc.).

    If player win or round draw: show result message instead of current player.
    """
    help_1 = f'│{nums["1"]:^5s}│{nums["2"]:^5s}│{nums["3"]:^5s}│'
    help_2 = f'│{nums["4"]:^5s}│{nums["5"]:^5s}│{nums["6"]:^5s}│'
    help_3 = f'│{nums["7"]:^5s}│{nums["8"]:^5s}│{nums["9"]:^5s}│'

    board_1 = f'│{cells["1"]:^5s}│{cells["2"]:^5s}│{cells["3"]:^5s}│'
    board_2 = f'│{cells["4"]:^5s}│{cells["5"]:^5s}│{cells["6"]:^5s}│'
    board_3 = f'│{cells["7"]:^5s}│{cells["8"]:^5s}│{cells["9"]:^5s}│'

    header_line = '┌─────┬─────┬─────┐'
    middle_line = '├─────┼─────┼─────┤'
    footer_line = '└─────┴─────┴─────┘'

    scoreboard = f'"X"{scores["X"]:>4d} : {scores["O"]:<4d}"O"'
    round_data = f'Round {current_round}'
    if not result:
        current_info = f'Player "{player}"'
    else:
        if result == 'win':
            message = f'Player "{player}" wins the round!'
            highlight = green_color
        else:
            message = 'It\'s a draw - nobody wins.'
            highlight = yellow_color
        current_info = f'{highlight}{message:^30}{end_color}'

    print_logo()
    print(f'{header_line}{"SCORE":^30}{header_line}')
    print(f'{help_1}{scoreboard:^30}{board_1}')
    print(f'{middle_line}{"":^30}{middle_line}')
    print(f'{help_2}{round_data:^30}{board_2}')
    print(f'{middle_line}{"":^30}{middle_line}')
    print(f'{help_3}{current_info:^30}{board_3}')
    print(f'{footer_line}{"":^30}{footer_line}')


def ask_a_move():
    """Ask player to enter the cell number for a move, or "quit" for exit."""
    global player_input
    message = 'Enter the cell number or "quit"'
    player_input = input(f'{"":>18}{message}: ')


def cell_is_available():
    """Check if player input is one of available cells or "quit" command."""
    if player_input in nums.values():
        return True
    elif player_input == 'quit':
        return quit_game()
    return None


def show_error():
    """Show message if entered cell is taken or other if input is wrong."""
    if player_input in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        error_message = f'Cell "{player_input}" is already taken.'
    else:
        error_message = f'It\'s not a number of cell.'
    print(f'{red_color}{error_message:^68}{end_color}')


def save_a_move():
    """Mark & save chosen cell number as one of the current player cells."""
    cells[player_input] = player
    nums[player_input] = ' '
    players_cells[player].add(int(player_input))


def is_row_of_3_marks():
    """Return True if rows of 3 marks are exist on playing field."""
    global winning_rows
    winning_rows = [
        _ for _ in winning_cells if _.issubset(players_cells[player])
    ]
    if winning_rows:
        return True
    return None


def is_all_cells_filled():
    """Return True if all cells on playing field are filled."""
    if '' not in cells.values():
        return True
    return None


def change_player():
    """Switch current player between "X" and "O"."""
    global player
    if player == 'X':
        player = 'O'
    else:
        player = 'X'


def highlight_winning_rows():
    """Add green color to each mark in winning rows.

    If current console(terminal) app can display blinking
    ANSI escape sequences marks will be green & blinking.
    If not - just green.
    """
    for row in winning_rows:
        for cell in row:
            cell = str(cell)
            cells[cell] = f'{green_blink_color}{cells[cell]:^5}{end_color}'


def update_score():
    """Increase current player score by 1 point."""
    scores[player] += 1


def is_1000_score():
    """Return True if player has 1000 score.

    Show congrats, GAME OVER and countdown.
    """
    if 1000 in scores.values():
        print()
        print(f'{"Wow, 1000 scores! Take a rest.":^68}')
        print(f'{"GAME OVER":^68}')
        for _ in range(10, -1, -1):
            timer = f'{_:^68}'
            print(timer, end='\r')
            time.sleep(1)
        return True
    return None


def clear_screen():
    """Clear terminal screen. History available by scroll."""
    print("\033[H\033[2J", end="", flush=True)


def get_next_move(error=False):
    """Combine call of simple repeated functions to make code more DRY."""
    clear_screen()
    show_board()
    if error:
        show_error()
    else:
        print()
    ask_a_move()


def quit_game():
    """Print "Good bye!" and leave the game after 1 sec pause."""
    print()
    print(f'{"Good bye!":^68}')
    time.sleep(1)
    clear_screen()
    sys.exit()


def game():
    """Main script of the gameplay."""
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
    quit_game()


player = 'O'
current_round = 0
scores = {'X': 0, 'O': 0}
players_cells = {}
player_input = ''
nums = {}
cells = {}
winning_cells = [
    {1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {1, 4, 7},
    {2, 5, 8}, {3, 6, 9}, {1, 5, 9}, {3, 5, 7}
]
winning_rows = []

red_color = '\033[91;1m'
green_color = '\033[92;1m'
green_blink_color = '\033[92;5m'
yellow_color = '\033[93;1m'
end_color = '\033[0m'

if __name__ == '__main__':
    game()
