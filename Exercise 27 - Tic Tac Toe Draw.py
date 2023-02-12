def new_coordinates(player_coordinates):
    player_coordinates = player_coordinates.split(",")
    new_digits = [int(x) for x in player_coordinates]
    final_new_digits = []
    for number in new_digits:
        new_number = number - 1
        final_new_digits.append(new_number)
    return final_new_digits

def player1_action(boardgame):
    if boardgame[new_coordinates(player1_move)[0]][new_coordinates(player1_move)[1]] == 'x' or boardgame[new_coordinates(player1_move)[0]][new_coordinates(player1_move)[1]] == 'o':
        return 'This square is already occupied. Please try again. ' + player1_move
    else:
        boardgame[new_coordinates(player1_move)[0]][new_coordinates(player1_move)[1]] = 'x'    
        return boardgame

def player2_action(boardgame):
    if boardgame[new_coordinates(player2_move)[0]][new_coordinates(player2_move)[1]] == 'x' or boardgame[new_coordinates(player2_move)[0]][new_coordinates(player2_move)[1]] == 'o':
        return 'This square is already occupied. Please try again. ' + player2_move
    else:
        boardgame[new_coordinates(player2_move)[0]][new_coordinates(player2_move)[1]] = 'o'    
        return boardgame

#The actual game programme
instructions = 'Welcome to Tic Tac Toe. This is a two player game. I imagine you\'re familiar with the rules, if not, kindly ask for help. Both players will use tokens to state the squares they\'ve occupied. Player 1\'s token is "x" and player 2\'s token is "o".'
print(instructions)

game = [[0,0,0],
        [0,0,0],
        [0,0,0]]

player1_move = 0
player2_move = 0
count = 0

while count < 9:
    count = 0
    player1_move = input('Player One, kindly  state the coordinates of your next move (i.e. the top left square is 1,1): ')
    print(player1_action(game))

    for i in game:
            for j in i:
                if j == 'x' or j == 'o':
                    count += 1

    if count == 9:
                print('Game over')

    count = 0
    player2_move = input('Player Two, kindly state the coordinates of your next move (i.e. the top left square is 1,1): ')
    print(player2_action(game))

    for i in game:
            for j in i:
                if j == 'x' or j == 'o':
                    count += 1
