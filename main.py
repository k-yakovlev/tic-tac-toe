cells = {1: 'X', 2: 'O', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}

player_1_moves = {}
player_2_moves = {}

row_1 = f'{cells[1]:^3s}│{cells[2]:^3s}│{cells[3]:^3s}'
row_2 = f'{cells[4]:^3s}│{cells[5]:^3s}│{cells[6]:^3s}'
row_3 = f'{cells[7]:^3s}│{cells[8]:^3s}│{cells[9]:^3s}'

# print(row_1, row_2, row_3, sep='\n───┼───┼───\n')
# print()
logo = """

88888888888 d8b                888                            888                      
    888     Y8P                888                            888                      
    888                        888                            888                      
    888     888  .d8888b       888888  8888b.   .d8888b       888888  .d88b.   .d88b.  
    888     888 d88P"          888        "88b d88P"          888    d88""88b d8P  Y8b 
    888     888 888     888888 888    .d888888 888     888888 888    888  888 88888888 
    888     888 Y88b.          Y88b.  888  888 Y88b.          Y88b.  Y88..88P Y8b.     
    888     888  "Y8888P        "Y888 "Y888888  "Y8888P        "Y888  "Y88P"   "Y8888  
                                                                                       
                                                                                       
"""

print(logo)
print(22*' ' + ' 1 │ 2 │ 3 ' + 20*' ' + row_1)
print(22*' ' + '───┼───┼───' + 20*' ' + '───┼───┼───')
print(22*' ' + ' 4 │ 5 │ 6 ' + 20*' ' + row_2)
print(22*' ' + '───┼───┼───' + 20*' ' + '───┼───┼───')
print(22*' ' + ' 7 │ 8 │ 9 ' + 20*' ' + row_3)
