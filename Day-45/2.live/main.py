from bs4 import BeautifulSoup
import lxml
import requests

data = requests.get("https://news.ycombinator.com")
website = data.text
soup = BeautifulSoup(website,"lxml")


text = []
links = []
upvote = []

for i in soup.findall('span', {"class": "titleline"}):
    text.append(i.getText())

# print(text)

links = soup.findall('span',{'class' : 'sitestr'}).getText()
