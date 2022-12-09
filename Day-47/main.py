from bs4 import BeautifulSoup
import smtplib
import requests
import pandas as pd
import html5lib


class Amazon_Scrapper():

    def __init__(self):
        print("----Enter Tech items only----")
        self.search_query = input(
            '\nEnter your search query:').replace(" ", "+")
        self.base_url = f"https://www.amazon.in/s?k={self.search_query}"
        self.headers = {
            "User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
        }

    def scraping(self):
        """ attributes of the products procured from the page"""
        self.product_name_list = []
        self.price_list = []
        self.rating_list = []

        self.soup = BeautifulSoup(requests.get(
            self.base_url, headers=self.headers).text, 'html5lib')
        self.data = self.soup.find_all(
            'div', class_="s-card-container s-overflow-hidden aok-relative puis-include-content-margin puis s-latency-cf-section s-card-border")
        for self.product in self.data:
            self.product_name = self.product.find(
                "span", class_="a-price-whole")
            self.product_name_list.append(self.product_name.getText().strip())

            # self.price = self.product.find('div',class_ ="a-row a-size-base a-color-base")
            # self.price_list.append(self.price.getText().strip())

        print("----Products ---")
        [print(i) for i in self.product_name_list]

    def output(self):
        self.product_name_pandas = pd.Series(self.product_name_list)
        self.price_name_pandas = pd.Series(self.price_list)
        self.frame = {"Product": self.product_name_pandas,
                      "Price": self.price_name_pandas}
        self.result = pd.DataFrame(self.frame)
        print(self.result)
        self.result.to_csv("output.csv")

    def email(self):
        pass

    def excel(self):
        pass


product = Amazon_Scrapper()
product.scraping()
product.output()
