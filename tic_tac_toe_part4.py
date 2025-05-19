

game = [[0,0,0],
        [0,0,0],
        [0,0,0]]

def play_game(player=0, row=0, column=0, just_display=False):
    print ("   0  1  2")
    if not just_display:
        game[row][column] = player
    for count, i in enumerate(game):
        print(count,i)
play_game(1,2,2,False)