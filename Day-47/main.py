import datetime
from bs4 import BeautifulSoup
import smtplib
import requests
import pandas as pd


class Amazon_Scrapper():

    def __init__(self):
        print("----Enter Tech items only----")
        self.search_query = input('\nEnter your search query:').replace(" ", "+")
        self.base_url = f"https://www.amazon.in/s?k={self.search_query}"
        self.headers = {
            "User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
        }

    def scraping(self):
        """ attributes of the products procured from the page"""
        self.product_name_list = []
        self.rating = []
        self.soup = BeautifulSoup(requests.get(
            self.base_url, headers=self.headers).text, 'html.parser')
        self.data = self.soup.find_all(
            'div', class_="s-card-container s-overflow-hidden aok-relative puis-include-content-margin puis s-latency-cf-section s-card-border")
        for self.product in self.data:
            self.product_name = self.product.find(
                "span", class_="a-size-medium a-color-base a-text-normal")
            self.product_name_list.append(self.product_name.getText().strip())
        print("----Products ---")
        [print(i) for i in self.product_name_list]


"""for item in div:
    title = item.find("h3")
    print(title.getText().strip())
"""

product = Amazon_Scrapper()
product.scraping()
