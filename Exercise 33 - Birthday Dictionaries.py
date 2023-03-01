import time
start_time = time.time()
birthdays = {
    'Thierry Henry': '17/08/1977',
    'Megan Good': '08/08/1981',
    'Lil Uzi Vert': '31/07/1995'
}
print('Welcome to the birthday dictionary. We know the birthdays of:')
for name in birthdays.keys():
  print(name)

ask = input('Whose birthday do you want to look up?: ')
print('{}\'s birthday is {}.'.format(ask, birthdays.get(ask, '- Oops try again and type the name just like the example shown.')))
print("--- %s seconds ---" % (time.time() - start_time))
