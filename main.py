import random


def ask_new_game(attempt):
    """Ask user to play a game of tic-tac-toe."""
    if attempt == 1:
        answer = input('Wanna play? (y/n): ')
    else:
        words = ['Enter', 'Type', 'Only', 'Just', 'WARNING:']
        word = random.choice(words)
        answer = input(f'{word} "y" (as "yes") to play or "n" (as "no") to leave the game: ')

    if answer.lower() == 'y':
        return
    elif answer.lower() == 'n':
        return
    ask_new_game(attempt=2)


logo = """
,--------.,--.               ,--.                         ,--.                 
'--.  .--'`--' ,---.,-----.,-'  '-. ,--,--. ,---.,-----.,-'  '-. ,---.  ,---.  
   |  |   ,--.| .--''-----''-.  .-'' ,-.  || .--''-----''-.  .-'| .-. || .-. : 
   |  |   |  |\ `--.         |  |  \ '-'  |\ `--.         |  |  ' '-' '\  ---. 
   `--'   `--' `---'         `--'   `--`--' `---'         `--'   `---'  `----' 

"""

# nums = {'1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9'}
# cells = {'1': '', '2': '', '3': '', '4': '', '5': '', '6': '', '7': '', '8': '', '9': ''}
#
# player_x_cells = []
# player_o_cells = []


# players = ['', 'X', 'O']
# scores = {'X': 0, 'Y': 0}
# i = 1
#
# while '' in cells.values():
#     help_1 = f'{nums["1"]:^5s}│{nums["2"]:^5s}│{nums["3"]:^5s}'
#     help_2 = f'{nums["4"]:^5s}│{nums["5"]:^5s}│{nums["6"]:^5s}'
#     help_3 = f'{nums["7"]:^5s}│{nums["8"]:^5s}│{nums["9"]:^5s}'
#
#     result_1 = f'{cells["1"]:^5s}│{cells["2"]:^5s}│{cells["3"]:^5s}'
#     result_2 = f'{cells["4"]:^5s}│{cells["5"]:^5s}│{cells["6"]:^5s}'
#     result_3 = f'{cells["7"]:^5s}│{cells["8"]:^5s}│{cells["9"]:^5s}'
#
#     separator = '─────┼─────┼─────'
#
#     current_player = f'Player "{players[i]}"'
#
#     print('\n' * 100)
#     print(logo)
#     print(3*' ' + help_1 + 38*' ' + result_1)
#     print(3*' ' + separator + 38*' ' + separator)
#     print(3*' ' + help_2 + f'{current_player:^38s}' + result_2)
#     print(3*' ' + separator + 38*' ' + separator)
#     print(3*' ' + help_3 + 38*' ' + result_3)
#     print()
#     player_input = input(f'{"":>28s}Enter the cell number: ')
#
#     if player_input in nums.values():
#         cells[player_input] = players[i]
#         nums[player_input] = ' '
#
#     i = -i

if __name__ == '__main__':
    print(logo)
    ask_new_game(attempt=1)
