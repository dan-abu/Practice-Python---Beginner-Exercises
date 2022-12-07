# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus
# all the duplicates.

# Extras:

# Write two different functions to do this - one using a loop and constructing a list, and another using sets.
# Go back and do Exercise 5 using sets, and write the solution for that in a different function.

c = [1, 1, 2, 2, 2, 3, 4, 5]

# Loop method
def remove_dupes(lst):
    new_list = []
    for num in lst:
        if num not in new_list:
            new_list.append(num)
    return new_list

print(remove_dupes(c))

# Set method

def remove_dupes2(lst):
    lst = set(lst)
    return lst

print(remove_dupes2(c))

# Re-doing exercise 5 with sets
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def remove_dupes3(lst1, lst2):
    new_list = []
    lst1 = set(lst1)
    lst2 = set(lst2)
    for x in lst1:
        if x in lst2:
            new_list.append(x)
    return new_list

print(remove_dupes3(a, b))