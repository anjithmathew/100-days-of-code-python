from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class Amazon():
    def __init__(self):
        self.website = "https://www.python.org/"
        self.path = "/home/toor/Downloads/chromedriver"

    def access(self):
        self.driver = webdriver.Chrome(self.path)
        self.driver.get(self.website)
        self.x = self.driver.find_element(By.XPATH,"/html/body/div/footer/div[2]/div/ul/li[3]/a")
        print(self.x.text)





a = Amazon()
a.access()