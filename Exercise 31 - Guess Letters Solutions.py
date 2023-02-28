# Let’s continue building Hangman. In the game of Hangman, a clue word is given by the program that the player has to guess, letter by letter. The player
# guesses one letter at a time until the entire word has been guessed. (In the actual game, the player can only guess 6 letters incorrectly before losing).

# Let’s say the word the player has to guess is “EVAPORATE”. For this exercise, write the logic that asks a player to guess a letter and displays letters in the
# clue word that were guessed correctly. For now, let the player guess an infinite number of times until they get the entire word. As a bonus, keep track of the
# letters the player guessed and display a different message if the player tries to guess that letter again. Remember to stop the game when all the letters have been
# guessed correctly! Don’t worry about choosing a word randomly or keeping track of the number of guesses the player has remaining - we will deal with those
# in a future exercise.

import time
import random
start_time = time.time()

s = open('/content/drive/MyDrive/Colab Notebooks/sowpods.txt', 'r')
sowpod = s.read().split()
s.close()

h_word = sowpod[random.randint(0, len(sowpod))]
h_word_list = list(h_word)
guess_word_range = range(0, len(h_word))
guess_word = []
for x in guess_word_range:
  guess_word.append('_')

print('Welcome to Hangman!')

while guess_word != h_word_list:
  print(' '.join(guess_word)) 
  guess = input('Guess your letter (caps only): ')
  if guess in h_word_list:
    for count, letter in enumerate(h_word_list):
      if letter == guess:
        guess_word[count] = guess
  else:
      print('Incorrect - try again!')

else:
  print('Congratulations - you\'ve guessed the right word: ', ''.join(guess_word))

print("--- %s seconds ---" % (time.time() - start_time))
