# write a program that prints out all the elements of a list that are less than 5.

# Extras:
# 1.) Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it
# and print out this new list.
# 2.) Write this in one line of Python.
# 3.) Ask the user for a number and return a list that contains only elements from the original list a that are smaller than
# that number given by the user.

# Solution to the initial task
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for x in a:
#     if x < 5:
#         print(x)

# Solution to the first extra task
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = []
# for x in a:
#     if x < 5:
#         b.append(x)
# print(b)

# Solution to the second extra task
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [x for x in a if x < 5]
# print(b)

# Solution to the third extra task
num = int(input('Kindly select a number: '))
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [x for x in a if x < num]
print(b)