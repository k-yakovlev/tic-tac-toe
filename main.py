cells = {1: 'X', 2: 'O', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}
nums = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

player_x_cells = []
player_o_cells = []

row_1 = f'{cells[1]:^5s}│{cells[2]:^5s}│{cells[3]:^5s}'
row_2 = f'{cells[4]:^5s}│{cells[5]:^5s}│{cells[6]:^5s}'
row_3 = f'{cells[7]:^5s}│{cells[8]:^5s}│{cells[9]:^5s}'

logo = """
,--------.,--.               ,--.                         ,--.                 
'--.  .--'`--' ,---.,-----.,-'  '-. ,--,--. ,---.,-----.,-'  '-. ,---.  ,---.  
   |  |   ,--.| .--''-----''-.  .-'' ,-.  || .--''-----''-.  .-'| .-. || .-. : 
   |  |   |  |\ `--.         |  |  \ '-'  |\ `--.         |  |  ' '-' '\  ---. 
   `--'   `--' `---'         `--'   `--`--' `---'         `--'   `---'  `----' 

"""

players = ['', 'X', 'O']
i = 1

while '' in cells.values():
    current_player = f'Player "{players[i]}"'
    i = -i

    print('\n' * 100)
    print(logo)
    print(3*' ' + f'  {nums["1"]}  │  {nums["2"]}  │  {nums["3"]}  ' + 38*' ' + row_1)
    print(3*' ' + '─────┼─────┼─────' + 38*' ' + '─────┼─────┼─────')
    print(3*' ' + f'  {nums["4"]}  │  {nums["5"]}  │  {nums["6"]}  ' + f'{current_player:^38s}' + row_2)
    print(3*' ' + '─────┼─────┼─────' + 38*' ' + '─────┼─────┼─────')
    print(3*' ' + f'  {nums["7"]}  │  {nums["8"]}  │  {nums["9"]}  ' + 38*' ' + row_3)
    print()
    player_input = input(f'{"":>28s}Enter the cell number: ')
    if player_input in nums.keys():
        nums[player_input] = ' '
