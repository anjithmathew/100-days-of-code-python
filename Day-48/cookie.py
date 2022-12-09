from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


class game():
    def __init__(self):
        self.website = "http://orteil.dashnet.org/experiments/cookie/"
        self.path = "/home/toor/Downloads/chromedriver"

    def automation(self):
        self.chrome_options = Options()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=Service(
            ChromeDriverManager().install()), options=self.chrome_options)
        self.driver.get(self.website)

        "clicking the first language element"



        # self.language_element = self.find_element(
        #     By.ID, "cookie"  )
        # self.language_element.click

        self.cookie = self.find_element(BY.ID,"cookie")
        print(self.cookie.text)


cookie = game()
cookie.automation()
