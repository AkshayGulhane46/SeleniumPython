from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:/Users\Android - PC\Downloads\drivers\chromedriver.exe")
driver.get("https://testautomationpractice.blogspot.com/")

driver.switch_to.frame(0)

driver.find_element_by_id("RESULT_FileUpload-11").send_keys("C://Users/Android - PC/Pictures/pc40.PNG")



#you can add any number of files 

