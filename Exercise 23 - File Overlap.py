# Given two .txt files that have lists of numbers in them, find the numbers that are overlapping. One .txt file has a list of all prime numbers under 1000, and the
# other .txt file has a list of happy numbers up to 1000.

import time
start_time = time.time()

with open('/content/drive/MyDrive/Colab Notebooks/primenumbers.txt', 'r') as open_file:
    all_text = open_file.read()

p_list = all_text.split('\n')

with open('/content/drive/MyDrive/Colab Notebooks/happynumbers.txt', 'r') as open_file:
    all_text = open_file.read()

h_list = all_text.split('\n')

primelist = []
for x in p_list:
  x = int(x)
  primelist.append(x)

happylist = []
for x in h_list:
  x = int(x)
  happylist.append(x)

print(primelist)
print(happylist)

mutual_list = []
for x in primelist:
  if x in happylist:
    mutual_list.append(x)

print(mutual_list)

print("--- %s seconds ---" % (time.time() - start_time))
