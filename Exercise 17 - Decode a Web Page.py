# Use the BeautifulSoup and requests Python packages to print out a list of all the article
# titles on the New York Times homepage.

import requests
from bs4 import BeautifulSoup
url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text
soup = BeautifulSoup(r_html,"html.parser")
headlines = [headline.get_text() for headline in soup.find_all('h3')]
headlines.remove('Advertisement')

for headline in headlines:
    print(headline)