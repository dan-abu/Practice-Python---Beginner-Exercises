# The exercise comes first (with a few extras if you want the extra challenge or want to spend more time), followed by a
# discussion. Enjoy!
# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
# Hint: how does an even / odd number react differently when divided by 2?

# Extras:
# 1.) If the number is a multiple of 4, print out a different message.
# 2.) Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
# If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

# Solution to the intial task
# number = int(input("Kindly insert a number at random: "))
# if number % 2 == 0:
#     print("You have inserted an even number.")
# else:
#     print("You have inserted an odd number.")

# Solution to the first extra task
# number = int(input("Kindly insert a number at random: "))
# if number % 2 == 0 and number % 4 == 0:
#     print("You have inserted an even number and a number divisible by four.")
# else:
#     print("You have inserted an odd number.")

# Solution to the second extra task
num = int(input("Kindly insert a number at random: "))
check = int(input("Kindly insert another number: "))
if num % check == 0:
    print("Your first number is divisible by your second number.")
else:
    print("Your first number is not divisible by your second number.")