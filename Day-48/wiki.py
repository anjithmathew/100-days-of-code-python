from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome()

driver.get("https://en.wikipedia.org/wiki/Main_Page")

x = driver.find_element(By.LINK_TEXT,"Raorchestes chalazodes")

y= driver.find_element(By.NAME,"search")
y.send_keys("python")
y.send_keys(Keys.ENTER)
time.sleep(10000000000)

opts = ChromeOptions()
opts.add_experimental_option("detach", True)
driver = Chrome(chrome_options=opts)
