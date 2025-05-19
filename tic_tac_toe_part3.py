game = [[0,0,0],
        [0,0,0],
        [0,0,0]]

'''print ("   a  b  c")
for count, i in enumerate(game):
    print(count,i)

game[0][1]= 1
print ("   a  b  c")
for count, i in enumerate(game):
    print(count,i)

game [1][1] = 2

print ("   a  b  c")
for count, i in enumerate(game):
    print(count,i)'''

#instead of repeating the code as above for each move, we can create a function

def play_game():
    print ("   a  b  c")
    for count, i in enumerate(game):
        print(count,i)

play_game()