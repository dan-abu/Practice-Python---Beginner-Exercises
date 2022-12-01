# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only
# the first and last elements of the given list. For practice, write this code inside a function.

# Returning the start and end of a list containing random numbers
def list_ends():
    import random
    numbers = random.sample(range(1, 51), 12)
    new_numbers = []
    new_numbers.append(numbers[0])
    new_numbers.append(numbers[-1])
    return new_numbers

print(list_ends())

# Returning the start and end of a list of numbers provided by the user
def other_list_ends(your_list):
    return [your_list[0], your_list[len(your_list)-1]]