'''game = "I want to play a game"
print(id(game)) #1

def play_game(player=0, row=0, column=0, just_display=False):
    global game
    print(game)
    game = "Changed mind, not playing"
    print(game)
    print(id(game)) #!1

play_game()
print(game)
print(id(game))#1'
'''

'''game=[1,2,3]
print(id(game))

def game_board(player=0, row=0, column=0, just_display=False):
    #global game
    print(game)
    game=[0,2,3]
    print(game)
    print(id(game))

game_board()
print(game)
print(id(game))'''

game=[1,2,3]
print(game)
print(id(game))

def game_board(player=0, row=0, column=0, just_display=False):
    #global game
    game[1]=99
    print(game)
    print(id(game))

game_board()
print(game)
print(id(game))