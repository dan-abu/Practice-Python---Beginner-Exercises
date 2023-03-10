import time
import datetime
start_time = time.time()

now = datetime.datetime.now()
name = str(input("Please state your name here: "))
age = int(input("Please state your age here: "))
centenaryyear = str(now.year+(100-age))

print(f"Dear {name}, it is a pleasure to meet you. You will be one hundred years old in {centenaryyear}.")
print("--- %s seconds ---" % (time.time() - start_time))
