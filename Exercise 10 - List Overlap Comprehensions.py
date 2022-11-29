# Take two lists, and write a program that returns a list that contains only the elements that are common between the
# lists (without duplicates). Make sure your program works on two lists of different sizes. Write this in one line of
# Python using at least one list comprehension. (Hint: Remember list comprehensions from Exercise 7).

# The original formulation of this exercise said to write the solution using one line of Python, but a few readers
# pointed out that this was impossible to do without using sets that I had not yet discussed on the blog, so you can either
# choose to use the original directive and read about the set command in Python 3.3, or try to implement this on your own and
# use at least one list comprehension in the solution.

# Extra:

# Randomly generate two lists to test this
import random

a = random.sample(range(1, 50), 8)
a = set(a)

b = random.sample(range(1, 50), 12)
b = set(b)

c = [x for x in a if x in b]
print(c)