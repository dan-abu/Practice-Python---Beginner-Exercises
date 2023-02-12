# This exercise is Part 2 of 4 of the Tic Tac Toe exercise series. The other exercises are: Part 1, Part 3, and Part 4.

# As you may have guessed, we are trying to build up to a full tic-tac-toe board. However, this is significantly more than half an hour of coding, so we’re doing it in pieces.

# Today, we will simply focus on checking whether someone has WON a game of Tic Tac Toe, not worrying about how the moves were made.

# If a game of Tic Tac Toe is represented as a list of lists, like so:

# game = [[1, 2, 0],
# 	[2, 1, 0],
# 	[2, 1, 1]]
# where a 0 means an empty square, a 1 means that player 1 put their token in that space, and a 2 means that player 2 put their token in that space.

# Your task this week: given a 3 by 3 list of lists that represents a Tic Tac Toe game board, tell me whether anyone has won, and tell me which player won, if any. A Tic
# Tac Toe win is 3 in a row - either in a row, a column, or a diagonal. Don’t worry about the case where TWO people have won - assume that in every board there will only be one 
# winner.

def check_tic_tac_toe(a, b, c):
    if a == [1, 1, 1] or b == [1, 1, 1] or c == [1, 1, 1]: #winning row code
        return 'Player one wins'
    elif a == [2, 2, 2] or b == [2, 2, 2] or c == [2, 2, 2]: #winning row code
        return 'Player two wins'
    elif [a[0], b[1], c[2]] == [1, 1, 1]: #winning diagonal code
        return 'Player one wins'
    elif [a[2], b[1], c[0]] == [1, 1, 1]: #winning diagonal code
        return 'Player one wins'
    elif [a[0], b[1], c[2]] == [2, 2, 2]: #winning diagonal code
        return 'Player two wins'
    elif [a[2], b[1], c[0]] == [2, 2, 2]: #winning diagonal code
        return 'Player two wins'
    elif [a[0], b[0], c[0]] == [1, 1, 1] or [a[1], b[1], c[1]] == [1, 1, 1] or [a[2], b[2], c[2]] == [1, 1, 1]:
        return 'Player one wins'
    elif [a[0], b[0], c[0]] == [2, 2, 2] or [a[1], b[1], c[1]] == [2, 2, 2] or [a[2], b[2], c[2]] == [2, 2, 2]:
        return 'Player two wins'
    else:
      return 'No one has won'

# Example gameboard to be used in the function
game = [[1, 2, 0], [2, 1, 2], [0, 1, 1]]
print(check_tic_tac_toe(game[0], game[1], game[2]))
