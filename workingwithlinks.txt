#how many links present we can validate
#capture all the links in a webpage

from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome(executable_path="C:/Users\Android - PC\Downloads\drivers\chromedriver.exe")
driver.get("https://www.seleniumhq.org/download/")
links=driver.find_elements(By.TAG_NAME, "a")
print(len(links))

