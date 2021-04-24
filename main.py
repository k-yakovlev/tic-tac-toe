cells = {1: 'X', 2: 'O', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}

player_1_moves = {}
player_2_moves = {}

row_1 = f'{cells[1]:^3s}│{cells[2]:^3s}│{cells[3]:^3s}'
row_2 = f'{cells[4]:^3s}│{cells[5]:^3s}│{cells[6]:^3s}'
row_3 = f'{cells[7]:^3s}│{cells[8]:^3s}│{cells[9]:^3s}'

# print(row_1, row_2, row_3, sep='\n───┼───┼───\n')
# print()

print(' 1 │ 2 │ 3 ' + 15*' ' + row_1)
print('───┼───┼───' + 15*' ' + '───┼───┼───')
print(' 4 │ 5 │ 6 ' + 15*' ' + row_2)
print('───┼───┼───' + 15*' ' + '───┼───┼───')
print(' 7 │ 8 │ 9 ' + 15*' ' + row_3)
