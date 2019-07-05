from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome(executable_path="C:/Users\Android - PC\Downloads\drivers\chromedriver")

driver.get("http://demo.automationtesting.in/Windows.html")

driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()

print(driver.current_window_handle)

# CD window - 4017C624390FFAD3BE495424768D30B1 parent window handle

handles = driver.window_handles  # return all the window handles values of all opened browser windows

for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
    if driver.title=="Frames & windows":
        driver.close()
        
driver.quit()        
        
        












