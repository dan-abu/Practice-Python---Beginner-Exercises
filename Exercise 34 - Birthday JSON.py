import time
import json
start_time = time.time()
with open("birthdays.json", "r") as f:
    birthdays = json.load(f)

def new_celeb_birthday(collection, json_f):
  new_celeb = input('What\'s the name of the celebrity you\'d like to add to our collection?: ')
  new_birthday = input('What\'s their birthday(DD/MM/YYYY)?: ')
  collection[new_celeb] = new_birthday
  with open(json_f, "w") as f:
    json.dump(collection, f)
  print('Thank you. We have added {} to our collection. See our collection of celebrity birthdays below.'.format(new_celeb))
  for name in collection.keys():
    print(name)

new_celeb_birthday(birthdays, 'birthdays.json')
print("--- %s seconds ---" % (time.time() - start_time))
