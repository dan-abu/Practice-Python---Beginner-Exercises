# Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of
# lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password
# every time the user asks for a new password. Include your run-time code in a main method.

# Extra:

# Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.

import time
start_time = time.time()
import string
import secrets
import random
import nltk
nltk.download('words')
from nltk.corpus import words
word_list = words.words()

def get_pwd_strength(help_txt='How strong would you like your password to be? (Choose between weak, medium and strong): '):
    pwd_strength = str(input(help_txt))
    if pwd_strength == 'weak' or pwd_strength == 'medium' or pwd_strength == 'strong':
            return pwd_strength
    while pwd_strength != 'weak' or pwd_strength != 'medium' or pwd_strength != 'strong':
        print('Please select weak, medium or strong.')
        pwd_strength = str(input(help_txt))
        if pwd_strength == 'weak' or pwd_strength == 'medium' or pwd_strength == 'strong':
            return pwd_strength
    
def get_pwd_limit(pwd_strength, help_txt='Kindly select how many characters you\'d like in your password (3-7 inclusive for weak, 8-11 inclusive for medium, 12+ for strong): '):
    pwd_limit = int(input(help_txt))
    if pwd_strength == 'weak':
        if 3 <= pwd_limit <= 7:
            return pwd_limit
        while not 3 <= pwd_limit <= 7:
            print('Please select an integer between 3 & 7 incllusive.')
            pwd_limit = int(input(help_txt))
            if 3 <= pwd_limit <= 7:
                return pwd_limit
    elif pwd_strength == 'medium':
        if 8 <= pwd_limit <= 11:
            return pwd_limit
        while not 8 <= pwd_limit <= 11:
            print('Please select an integer between 8 & 11 inclusive.')
            pwd_limit = int(input(help_txt))
            if 8 <= pwd_limit <= 11:
                return pwd_limit
    elif pwd_strength == 'strong':
        if pwd_limit >= 12:
            return pwd_limit
        while not pwd_limit >= 12:
            print('Please select an integer greater than or equal to 12.')
            pwd_limit = int(input(help_txt))
            if pwd_limit >= 12:
                return pwd_limit

def pwd_gen(pwd_limit):
    pwd_words = [word for word in word_list if 3 <= len(word) <= 7]
    letters = string.ascii_letters + string.digits + string.punctuation
    if 3 <= pwd_limit <= 7:
        password = random.choice([option for option in pwd_words if len(option) == pwd_limit])
        return password
    elif pwd_limit > 8:
        password = ''.join(secrets.choice(letters) for i in range(pwd_limit))
        return password

print(pwd_gen(get_pwd_limit(get_pwd_strength())))
print("--- %s seconds ---" % (time.time() - start_time))
