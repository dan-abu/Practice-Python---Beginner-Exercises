# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message
# of congratulations to the winner, and ask if the players want to start a new game)

# Remember the rules:

# Rock beats scissors
# Scissors beats paper
# Paper beats rock
while True:
    player1 = input('Select rock, paper, or scissors: ')
    player2 = input('Select rock, paper, or scissors: ')

    if player1 == player2:
        print('Draw')
        break

    elif player1 == 'rock' and player2 == 'scissors':
        print('Player one wins')
        break

    elif player1 == 'scissors' and player2 == 'paper':
        print('Player one wins')
        break

    elif player1 == 'paper' and player2 == 'rock':
        print('Player one wins')
        break

    elif player2 == 'rock' and player1 == 'scissors':
        print('Player two wins')
        break

    elif player2 == 'scissors' and player1 == 'paper':
        print('Player two wins')
        break

    elif player2 == 'paper' and player1 == 'rock':
        print('Player two wins')
        break

    else:
        print('Invalid input. Try again.')
