# Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file, and print out the
# results to the screen. I have a .txt file for you, if you want to use it!
import time
start_time = time.time()

with open('nameslist.txt', 'r') as open_file:
    all_text = open_file.read()

new_list = all_text.split('\n')
print(len(new_list))

with open('Training_01.txt', 'r') as open_file:
    text = open_file.read()

new_page = text.split('\n')
categories = []
for category in new_page:
    category = category[3:-25]
    categories.append(category)
categories = set(categories)
print(len(categories))
for category in categories:
    print(category)

print("--- %s seconds ---" % (time.time() - start_time))