# This exercise is Part 3 of 4 of the Tic Tac Toe exercise series. The other exercises are: Part 1, Part 2, and Part 4.

# In a previous exercise we explored the idea of using a list of lists as a “data structure” to store information about a tic tac toe game. In a tic tac toe game,
# the “game server” needs to know where the Xs and Os are in the board, to know whether player 1 or player 2 (or whoever is X and O won).

# There has also been an exercise about drawing the actual tic tac toe gameboard using text characters.

# The next logical step is to deal with handling user input. When a player (say player 1, who is X) wants to place an X on the screen, they can’t just click on a
# terminal. So we are going to approximate this clicking simply by asking the user for a coordinate of where they want to place their piece.

# As a reminder, our tic tac toe game is really a list of lists. The game starts out with an empty game board like this:

# game = [[0, 0, 0],
# 	[0, 0, 0],
# 	[0, 0, 0]]
# The computer asks Player 1 (X) what their move is (in the format row,col), and say they type 1,3. Then the game would print out

# game = [[0, 0, X],
# 	[0, 0, 0],
# 	[0, 0, 0]]
# And ask Player 2 for their move, printing an O in that place.

# Things to note:

# For this exercise, assume that player 1 (the first player to move) will always be X and player 2 (the second player) will always be O.
# Notice how in the example I gave coordinates for where I want to move starting from (1, 1) instead of (0, 0). To people who don’t program, starting to count at
# 0 is a strange concept, so it is better for the user experience if the row counts and column counts start at 1. This is not required, but whichever way you choose to
# implement this, it should be explained to the player.
# Ask the user to enter coordinates in the form “row,col” - a number, then a comma, then a number. Then you can use your Python skills to figure out which row and
# column they want their piece to be in.
# # Don’t worry about checking whether someone won the game, but if a player tries to put a piece in a game position where there already is another piece, do not allow
# the piece to go there.
# # Bonus:

# # For the “standard” exercise, don’t worry about “ending” the game - no need to keep track of how many squares are full. In a bonus version, keep track of how many
# squares are full and automatically stop asking for moves when there are no more valid moves.

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
