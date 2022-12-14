# Take the code from the How To Decode A Website exercise (if you didn’t do it or just want to play with some different code,
# use the code from the solution), and instead of printing the results to a screen, write the results to a txt file. In your
# code, just make up a name for the file you are saving to.

# Extras:

# Ask the user to specify the name of the output file that will be saved.

import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text
soup = BeautifulSoup(r_html,"html.parser")
headlines = [headline.get_text() for headline in soup.find_all('h3')]
headlines.remove('Advertisement')

open_file = open(str(input('Create your file name (no whitespace permitted and it must end in .py): ')), 'w')
for headline in headlines:
    open_file.write(str(headline))
open_file.close()