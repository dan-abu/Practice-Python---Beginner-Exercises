# Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)

# Solution
string = str(input("Enter a phrase or number. "))
rvstring = string[::-1]
if string == rvstring:
    print("This word is a palindrome")
else:
    print("This word is not a palindrome")