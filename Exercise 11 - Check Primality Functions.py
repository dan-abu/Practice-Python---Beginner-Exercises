# Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number
# is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to
# practice using functions, described below.

def get_integer(help_txt='Kindly select a number: '):
    return int(input(help_txt))

#importing solution from exercise 4 with improvements
user_number = get_integer()
options = range(1, (user_number+1))
divisors = []
for number in options:
    if user_number % number == 0:
        divisors.append(number)

if len(divisors) == 2:
    print('Your number is a prime number.')
else:
    print('Your number is not a prime number.')