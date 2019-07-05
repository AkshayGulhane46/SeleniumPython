from selenium import webdriver
driver=webdriver.Chrome(executable_path="C:/Users\Android - PC\Downloads\drivers\chromedriver.exe")
driver.get("http://newtours.demoaut.com/")  #url take some time to open

driver.implicitly_wait(10) #seconds

assert "Welcome:Mercury Tours" in driver.title

driver.find_element_by_name("userName").send_keys("mercury")
driver.find_element_by_name("password").send_keys("mercury")

driver.find_element_by_name("login").click()

#implicit wait is applicable for all the elements of the scrpit

#even though we put some time by the time element is not displayed we have a chance to get exception 
#it is based on time
#element is not available befor time then a exception is thrown