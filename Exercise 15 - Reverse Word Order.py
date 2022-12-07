# Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user
# the same string, except with the words in backwards order.

def get_string(help_txt='Kindly state a full sentence using more than two words and no punctuation: '):
    return str(input(help_txt))

def rev_word_order(og_sentence):
    new_sentence = og_sentence.split(' ')
    return new_sentence[::-1]

print(rev_word_order(get_string()))