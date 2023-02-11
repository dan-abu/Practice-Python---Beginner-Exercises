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
