import time
from selenium import webdriver

n=0
while(n<30):
    driver=webdriver.Chrome(executable_path="D:/appium\chromedriver.exe")
    driver.get("https://www.youtube.com/watch?v=Q-sgJ3xMJmg")
    time.sleep(10)
    n=n+1
    if (n>30):
        webdriver.close()









