# Implement a function that takes as input three variables, and returns the largest of the three. Do this without using the Python max() function!

# The goal of this exercise is to think about some internals that Python normally takes care of for us. All you need is some variables and if statements!

import time
start_time = time.time()

import random

a = random.randint(1,1000)
b = random.randint(1,1000)
c = random.randint(1,1000)

def max_of_three(one,two,three):
    if a > b and a > c:
        return str(a) + "(a) is the largest of the three variables."
    elif b > a and b > c:
        return str(b) + "(b) is the largest of the three variables."
    elif c > a and c > b:
        return str(c) + "(c) is the largest of the three variables."
    elif a == b == c:
        return "All three variables " + str(a, b, c) + "are the same. There is no largest variable."

print(max_of_three(a,b,c))
print("--- %s seconds ---" % (time.time() - start_time))
