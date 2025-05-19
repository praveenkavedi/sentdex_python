game = [[0,1,0],
       [0,0,0], 
       [0,0,0]]

def win(current_game):
    '''for item in current_game:
        print(item)'''
        all_mathces = True
        for item in current_game:
            if item != current_game[0]:
                all_mathces = False
        if all_mathces:
            print("Winner")
        else:
            print("No winner yet")
    
    
    
    '''for row in game:
    #matches =  False
        print(row, row[1])
        col0 = row[0]
        col1 = row[1]
        col2 = row[2]
        print(col0, col1, col2)
        if col0 == col1 == col2:
            print("Winner!")
        else:
            print("No winner yet")'''
win(game)