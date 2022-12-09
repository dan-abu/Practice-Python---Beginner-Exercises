# Create a program that will play the “cows and bulls” game with the user. The game works like this:

# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed correctly
# in the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong place is a “bull.” Every
# time the user makes a guess, tell them how many “cows” and “bulls” they have. Once the user guesses the correct number,
# the game is over. Keep track of the number of guesses the user makes throughout the game and tell the user at the end.
import random

random_num = str(random.randint(1000,10000))
print(random_num)
cows = 0
bulls = 0
guesses = 1
user_num = input("Kindly choose a four-digit number: ")
cows_and_bulls = {user_num[0]:random_num[0], user_num[1]:random_num[1], user_num[2]:random_num[2], user_num[3]:random_num[3]}
            
while True:
    for x in user_num:
            if x in random_num and x == cows_and_bulls[x]:
                cows += 1
            elif x in random_num and x != cows_and_bulls[x]:
                bulls += 1    
    
    if cows == 4:
        print(guesses, " guess(es)")
        print("4 cows. Congratulations - you've won.")
        break   
        
    else:
        print(guesses," guesses")
        print(str(cows) + " cows and " + str(bulls) + " bulls")
        cows = 0
        bulls = 0
        guesses += 1
        user_num = input("Kindly choose a four-digit number: ")
        cows_and_bulls = {user_num[0]:random_num[0], user_num[1]:random_num[1], user_num[2]:random_num[2], user_num[3]:random_num[3]}
        continue