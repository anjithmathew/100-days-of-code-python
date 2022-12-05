from bs4 import BeautifulSoup   
import requests

url = "https://www.billboard.com/charts/hot-100/"
soup = BeautifulSoup(requests.get(url).content,"html.parser")
div = soup.findAll("div",class_="o-chart-results-list-row-container")
for item in div:
    title = item.find("h3")
    print(title.getText().strip())

    




