from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver= webdriver.Chrome(executable_path=("C:/Users\Android - PC\Downloads\drivers\chromedriver.exe"))

driver.get("https://www.peopleskart.com/")
print(driver.title)

driver.get("https://www.cs-cart.my/")
time.sleep(5)
print(driver.title)
driver.back()
time.sleep(5)



