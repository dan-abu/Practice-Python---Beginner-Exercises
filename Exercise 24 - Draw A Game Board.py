# This exercise is Part 1 of 4 of the Tic Tac Toe exercise series. The other exercises are: Part 2, Part 3, and Part 4.

# Time for some fake graphics! Let’s say we want to draw game boards that look like this:

#  --- --- --- 
# |   |   |   | 
#  --- --- ---  
# |   |   |   | 
#  --- --- ---  
# |   |   |   | 
#  --- --- --- 
# This one is 3x3 (like in tic tac toe). Obviously, they come in many other sizes (8x8 for chess, 19x19 for Go, and many more).

# Ask the user what size game board they want to draw, and draw it for them to the screen using Python’s print statement.

# Remember that in Python 3, printing to the screen is accomplished by

#   print("Thing to show on screen")
# Hint: this requires some use of functions, as were discussed previously on this blog and elsewhere on the Internet, like this TutorialsPoint link.
import time
start_time = time.time()

def rows():
    return " --- \n"

def columns():
    return "|   |\n"
  
def more_rows():
    return " --- "

def more_columns():
    return "|   |"

def square_rows():
    if user_sq_num == 1:
        return rows()
    elif user_sq_num > 1:
        return (user_sq_num-1)*more_rows()

def square_columns():
    if user_sq_num == 1:
        return columns()
    elif user_sq_num > 1:
        return (user_sq_num-1)*more_columns()

def draw_a_game_board():
  user_sq_num = int(input("What size board game would you like? (e.g. 3 = 3x3, 4 = 4x4 etc.): "))
  if user_sq_num == 1:
    return(rows() + columns() + rows())
  elif user_sq_num > 1:
      return((square_rows() + rows()) + ((user_sq_num-1)*(square_columns() + columns() + square_rows() + rows())))
    
print(draw_a_game_board())

print("--- %s seconds ---" % (time.time() - start_time))
