import time
start_time = time.time()

name = str(input("Please state your name here: "))
age = int(input("Please state your age here: "))
centenaryyear = str(2023+(100-age))

print(f"Dear {name}, it is a pleasure to meet you. You will be one hundred years old in {centenaryyear}.")
print("--- %s seconds ---" % (time.time() - start_time))
