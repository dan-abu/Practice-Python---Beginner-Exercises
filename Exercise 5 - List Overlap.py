# Take two lists and write a program that returns a list that contains only the elements that are common between the lists
# (without duplicates). Make sure your program works on two lists of different sizes.

# Extras:
# 1.) Randomly generate two lists to test this
# 2.) Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)

# Solution to the initial task
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# mutual = []
# for x in a and b:
#     if x in a and b:
#         mutual.append(x)
# print(mutual)

# Solution to the first extra task
# import random
# a = random.sample(range(1, 50), 8)
# b = random.sample(range(1, 50), 12)
# print(a)
# print(b)
# mutual = []
# for x in a and b:
#     if x in a and b:
#         mutual.append(x)
# print(mutual)

# Solution to the second extra task
import random
a = random.sample(range(1, 50), 8)
b = random.sample(range(1, 50), 12)
print(a)
print(b)
mutual = [x for x in a and b if x in a and b]
print(mutual)