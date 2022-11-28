# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them
# whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from
# the very first exercise)

# Extras:

# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.
import random
rnum = random.randint(1,9)
user1 = int(input('Select a number between 1 and 9 (inclusive): '))
count = 1

while True:
    if user1 == rnum:
        print('You guessed correctly!')
        gbye = input('If you\'d like to leave the game, type \'exit\': ')
        if gbye == 'exit':
            print('This round took you', count, 'guess(es).')
            break

    elif user1 != rnum or user1 != 'exit':
        if user1 < rnum:
            print('Your guess is smaller than the correct answer. Try again.')
            count += 1
            user1 = int(input('Select a number between 1 and 9 (inclusive): '))
            continue

        elif user1 > rnum:
            print('Your guess is greater than the correct answer. Try again.')
            count += 1
            user1 = int(input('Select a number between 1 and 9 (inclusive): '))
            continue

#elif user1 == 'exit':
    #print('')