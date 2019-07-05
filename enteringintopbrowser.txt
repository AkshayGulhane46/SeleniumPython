from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="D:/appium\chromedriver.exe")
#driver=webdriver.Firefox(executable_path="C:/Users\Android - PC\Downloads\drivers\cgeckodriver.exe")
#driver2=webdriver.Ie(executable_path="C:/Users\Android - PC\Downloads\drivers\IEDriverServer.exe")

driver.get ('http://newtours.demoaut.com/')

print(driver.title) #title of page
print(driver.current_url)  #returns url of page
print(driver.page_source)  #HTML code of page

driver.close()
