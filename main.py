import requests
from bs4 import BeautifulSoup
import csv

URL = "https://en.wikipedia.org/wiki/Human%E2%80%93computer_interaction"

r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')

#print(soup.prettify())

urls = []
if r.status_code == 200:
    href = soup.find('div', id="content").find_all('a')
    for obj in href:
        st = str(obj).split()
        for o in st:
            if o.startswith('href') :
                urls.append("https://en.wikipedia.org" + o[6:-1])
myUrls = list(set(urls))
#print(myUrls)

urls = ""
filename = open("urls_from_wiki.txt", "a")
for url in myUrls:
    urls = str(url) + "\n"
    filename.write(urls)
filename.close()
