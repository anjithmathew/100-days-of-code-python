from bs4 import BeautifulSoup
import lxml
import requests

data = requests.get("https://news.ycombinator.com")
website = data.text
soup = BeautifulSoup(website,"lxml")

links = []


for link in soup.findAll('span', {"class": "titleline"}):
    links_of_web = link.get("a href")
    links.append(links_of_web)



