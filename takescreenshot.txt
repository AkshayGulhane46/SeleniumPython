from selenium import webdriver
driver=webdriver.Chrome(executable_path="D:/appium\chromedriver.exe")
driver.get("https://www.amazon.in/")
driver.save_screenshot("D:/appium\selenium with python\homepage.png")


#or you can use this method also
#driver.get_screenshot_as_file("D:/appium\selenium with python\page2.jpg")