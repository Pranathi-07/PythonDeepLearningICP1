from urllib.request import urlopen
from bs4 import BeautifulSoup
out_file = open('E:\\pythondeeplearning\\ICP3\\output', 'w')
url = "https://en.wikipedia.org/wiki/Deep_learning"
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')
type(soup)
title = soup.title.string
print(title)
for link in soup.find_all("a"):
    out_file.writelines(str(link.get('href')) + "\n")