#Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them
#the year that they will turn 100 years old.
#Note: for this exercise, the expectation is that you explicitly write out the year (and therefore be out of date the next year).

#Extras:
#1.) Add on to the previous program by asking the user for another number and printing out that many copies of the previous message.
#(Hint: order of operations exists in Python)
#2.) Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing
#the ENTER button)

#Solution to the initial task
#name = str(input("Please state your name here: "))
#age = int(input("Please state your age here: "))
#copies = int(input("Please choose a number: "))
#centenaryyear = str(2022+(100-age))
#print("Dear " + name + ", it is a pleasure to meet you. You will be one hundred years old in " + centenaryyear + ".")

#Solution to the first extra task
# name = str(input("Please state your name here: "))
# age = int(input("Please state your age here: "))
# copies = int(input("Please choose a number: "))
# centenaryyear = str(2022+(100-age))
# answer = ("Dear " + name + ", it is a pleasure to meet you. You will be one hundred years old in " + centenaryyear + ". ")
# print(copies * answer)

#Solution to the second extra task
name = str(input("Please state your name here: "))
age = int(input("Please state your age here: "))
copies = int(input("Please choose a number: "))
centenaryyear = str(2022+(100-age))
answer = ("Dear " + name + ", it is a pleasure to meet you. You will be one hundred years old in " + centenaryyear + ".\n")
print(copies * answer)