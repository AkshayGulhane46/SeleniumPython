from selenium import webdriver
import time
driver=webdriver.Chrome(executable_path="C:/Users\Android - PC\Downloads\drivers\chromedriver.exe")
driver.get("https://www.countries-ofthe-world.com/")
driver.find_element_by_xpath("//*[@id='topmenuul']/li[3]/a").click()
driver.maximize_window() # maximize window
time.sleep(2)

#scroll down page by pixel
#driver.execute_script("window.scrollBy(0,1000)", "") #ZERO POSITION TO HOW MANY

#scroll down page till element is visible
#flag=driver.find_element_by_xpath("//*[@id='content']/div[2]/div[2]/table[1]/tbody/tr[86]/td[2]")
#driver.execute_script("arguments[0].scrollIntoView();", flag)

#scroll down page till end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")






