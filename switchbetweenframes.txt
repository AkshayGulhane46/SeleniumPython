from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver= webdriver.Chrome(executable_path="C:/Users\Android - PC\Downloads\drivers\chromedriver.exe")

driver.get("https://seleniumhq.github.io/selenium/docs/api/java/index.html")
time.sleep(2)
driver.switch_to.frame("packageListFrame")  # first frame
time.sleep(2)
driver.find_element_by_link_text("org.openqa.selenium").click()
time.sleep(2)

driver.switch_to.default_content()
time.sleep(2)
driver.switch_to.frame("packageFrame")  # second frame

driver.find_element_by_link_text('WebDriver').click()
driver.switch_to.default_content()

driver.switch_to.frame("classFrame")   # third frame
driver.find_element_by_xpath("/html/body/div[1]/ul/li[5]/a").click()





