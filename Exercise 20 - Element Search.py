# Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest)
# and another number. The function decides whether or not the given number is inside the list and returns (then prints) an
# appropriate boolean.

# Extras:

# Use binary search.
def element_search():
    import random
    a = random.sample(range(1, 50), random.randint(1,9))
    a.sort()
    print(a)

    user_num = int(input('Kindly select an integer: '))
    
    if user_num in a:
        print('The number you selected is in the list.')
    else:
        print('The number you selected is not in the list.')

def binary_search():
    import random
    a = random.sample(range(1, 50), random.randint(1,9))
    a.sort()
    print(a)

    user_num = int(input('Kindly select an integer: '))

    if len(a) == 1:
        if user_num == a[0]:
            print('The number you selected is in the list.')
        else:
            print('The number you selected is not in the list.')    

    else:
        while True:
            if len(a) > 1:
                if len(a) % 2 == 0:
                    point = int((len(a)/2) - 1)
                    b = a[point::]
                    for num in b:
                        if user_num == num:
                            print('The number you selected is in the list.')
                            break
                        else:
                            a = a[0:point]
                            continue

                elif len(a) % 2 != 0:
                    point = int((len(a)/2) - 0.5)
                    b = a[point::]
                    for num in b:
                        if user_num == num:
                            print('The number you selected is in the list.')
                        else:
                            a = a[0:point]
                            continue
            elif len(a) == 1:
                if user_num == a[0]:
                    print('The number you selected is in the list.')
                    break  
                else:
                    print('The number you selected is not in the list.')
                    break