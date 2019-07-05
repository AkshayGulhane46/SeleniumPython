from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
driver= webdriver.Chrome(executable_path="C:/Users\Android - PC\Downloads\drivers\chromedriver.exe")

driver.get("https://testautomationpractice.blogspot.com/")

driver.maximize_window() #maximize the page

element = driver.find_element_by_xpath("//*[@id='HTML10']/div[1]/button")
actions=ActionChains(driver)
actions.double_click().perform()  # double click on element



