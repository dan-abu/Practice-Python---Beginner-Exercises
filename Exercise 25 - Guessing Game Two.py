# In a previous exercise, we’ve written a program that “knows” a number and asks
# a user to guess it.

# This time, we’re going to do exactly the opposite. You, the user, will have
# in your head a number between 0 and 100. The program will guess a number,
# and you, the user, will say whether it is too high, too low, or your number.

# At the end of this exchange, your program should print out how many guesses
# it took to get your number.

# As the writer of this program, you will have to choose how your program
# will strategically guess. A naive strategy can be to simply start the
# guessing at 1, and keep going (2, 3, 4, etc.) until you hit the number.
# But that’s not an optimal guessing strategy. An alternate strategy might
# be to guess 50 (right in the middle of the range), and then
# increase / decrease by 1 as needed. After you’ve written the program, try
# to find the optimal strategy! (We’ll talk about what is the optimal one next
# week with the solution.)
def guessing_game():
  import time
  start_time = time.time()

  c_options = range(0,101)
  c_index = int((len(c_options)/2))
  c_guess = c_options[c_index]
  guess = 1
  print(c_guess)
  user_check = str(input("Is this your number, or is it too high or too low? (Yes, too high or too low): "))

  while True:
    if user_check == 'Yes':
      print('I got it right in ', guess, ' guess(es)!')
      print("--- %s seconds ---" % (time.time() - start_time))
      break

    elif user_check == 'Too high':
      guess += 1
      if len(c_options) == 2:
        c_guess = c_options[0]
        print('This is your number: ', guess, '. I don\'t need you to tell me. I\'m amazing. I got it right in ', guess, ' guess(es)!')
        print("--- %s seconds ---" % (time.time() - start_time))
        break
      else:
        c_options = c_options[:c_index]
        c_index = int(len(c_options)/2)
        c_guess = c_options[c_index]
        print(c_guess)
        user_check = str(input("Is this your number, or is it too high or too low? (Yes, too high or too low): "))
        continue
      

    elif user_check == 'Too low':
      guess += 1
      if len(c_options) == 2:
        c_guess = c_options[1]
        print('This is your number: ', guess, '. I don\'t need you to tell me. I\'m amazing. I got it right in ', guess, ' guess(es)!')
        print("--- %s seconds ---" % (time.time() - start_time))
        break
      else:
        c_options = c_options[c_index:]
        c_index = int(len(c_options)/2)
        c_guess = c_options[c_index]
        print(c_guess)
        user_check = str(input("Is this your number, or is it too high or too low? (Yes, too high or too low): "))
        continue
        
guessing_game()
