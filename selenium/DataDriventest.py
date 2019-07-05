import XLUtils
from selenium import webdriver

driver=webdriver.Chrome(executable_path="D:/appium/chromedriver.exe")
driver.get("http://newtours.demoaut.com/")
driver.maximize_window()

path="C:/Users\Android - PC\Desktop\Login1.xlsx"

rows=XLUtils.getRowCount(path,'Sheet1')

for r in range(2,rows+1):
    username= XLUtils.readData(path,"Sheet1",r,1)
    password= XLUtils.readData(path,"Sheet1",r,2)
    driver.find_element_by_name("userName").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_name("login").click()
    if driver.title=="Find a Flight: Mercury Tours:":
        print("text is passed")
        XLUtils.writeData(path,"Sheet1",r,3,"test passed")
    else:
        print("test failed")
        XLUtils.writeData(path,"Sheet1",r,3,"test failed")

    driver.find_element_by_link_text("Home").click()