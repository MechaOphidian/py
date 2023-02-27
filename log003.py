import requests
from bs4 import BeautifulSoup

#get a page
r = requests.get('https://www.sacred-texts.com/')

#parse html
soup = BeautifulSoup(r.content, "html.parser")

#print soup.title
print(soup.title)

#prints the title name
print(soup.title.name)

#prints the parent title name
print(soup.title.parent.name)

topics = soup.find_all("span", {"class": "menutext"})
print(topics)