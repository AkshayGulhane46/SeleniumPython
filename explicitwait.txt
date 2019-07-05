# it works on condition not time
#suppose 10 elements we have to add 10 times explicit wait
#application and scenario 

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome(executable_path="C:/Users\Android - PC\Downloads\drivers\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.expedia.co.in/?AFFCID=IN.NETWORK.OMG.1868522.HOTEL-TEXTLINK&sskey=07fc8174686d4775b8969869ec3b99d8")
driver.find_element_by_id("tab-flight-tab-hp").click()
# driver.find_element_by_id(By.ID,"tab-flight-tab-hp").click()
#we clicked on flights button

time.sleep(2) #time is from python
driver.find_element_by_id("flight-origin-hp-flight").send_keys("NYC")
time.sleep(2)
driver.find_element_by_id("flight-destination-hp-flight").send_keys(("SFO"))

driver.find_element_by_id("flight-departing-hp-flight").clear()
driver.find_element_by_id("flight-departing-hp-flight").send_keys("10/7/2019")

driver.find_element_by_id("flight-returning-hp-flight").clear()
driver.find_element_by_id("flight-returning-hp-flight").send_keys("15/7/2019")

driver.find_element_by_xpath("//*[@id='gcw-flights-form-hp-flight']/div[8]/label/button").click()

wait=WebDriverWait(driver,10)# it will wait for 10 seconds if
                            #if element responds before 10 seconds then no provblem
                            #if not then error is thrown by code

#driver.find_element_by_xpath("//*[@id='stops']/div/div[3]").click()
element=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='stops']/div/div[3]")))
element.click()
time.sleep(6)
driver.quit()