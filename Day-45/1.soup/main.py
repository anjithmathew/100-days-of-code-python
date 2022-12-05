from bs4 import BeautifulSoup
import lxml

with open("/home/toor/Documents/1.Python/100-days-of-code-python/Day-45/website.html") as data:
    contents = data.read()

soup = BeautifulSoup(contents,  'lxml')
# print(soup.prettify())
# print(soup.ol.find_all())


anchor_taggs = soup.find_all(name="a")
print(anchor_taggs)


[print(tag.getText()) for tag in anchor_taggs]

[print(tag.get("href")) for tag in anchor_taggs]

section_heading = soup.find(name="h3", class_ ="heading")
print(section_heading.getText())

company_url = soup.select_one(selector="p a")
