from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver= webdriver.Chrome(executable_path="C:/Users\Android - PC\Downloads\drivers\chromedriver.exe")
driver.get("http://newtours.demoaut.com/")
user_ele=driver.find_element_by_name("userName")
print(user_ele.is_displayed())  #print true or false
print(user_ele.is_enabled()) #print true or false

pwd_ele=driver.find_element_by_name("password")
print(pwd_ele.is_displayed())  #print true or false
print(pwd_ele.is_enabled()) #print true or false

user_ele.send_keys("mercury")
pwd_ele.send_keys("mercury")

driver.find_element_by_name("login").click()
roundrip_radio=driver.find_element_by_css_selector("input[value=roundtrip]")
print("status of roundtrip radio",roundrip_radio.is_selected()) #print status of radio button
onetrip_radio=driver.find_element_by_css_selector("input[value=oneway]")
print("status of oneway radio",onetrip_radio.is_selected())


