
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#chrome
driver=webdriver.Chrome(executable_path="D:/appium\chromedriver.exe")
driver.get("https://www.google.com/")
print(driver.title)
print((driver.current_url))

driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div/div[3]/center/input[2]").click()
time.sleep(5)
driver.close()  #close current browser
driver.quit()  #close all opened browser