# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity
# to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence
# to generate.(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of
# the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

#Re-using code from exercise 11
def get_integer(help_txt='Kindly select a number: '):
    return int(input(help_txt))

def fibonacci():
    user_range = get_integer('Kindly select how many numbers you\'d like to see from the Fibonacci sequence: ')
    fibo = [1, 1]

    if user_range < 1:
        print('Please choose an integer greater than 0.')
        user_range = get_integer('Kindly select how many numbers you\'d like to see from the Fibonacci sequence: ')

    elif user_range == 1:
        print(fibo[0])

    elif user_range == 2:
        print(fibo)

    else:
        while fibo != user_range:
            fibo.append(fibo[-2] + fibo[-1])
            if len(fibo) == user_range:
                return fibo

print(fibonacci())