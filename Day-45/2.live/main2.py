from bs4 import BeautifulSoup
import requests
import json

url = "https://www.empireonline.com/movies/features/best-movies-2/"
soup = BeautifulSoup(requests.get(url).content,"html.parser")

data = json.loads(soup.select_one("#__NEXT_DATA__").contents[0])

print(data)