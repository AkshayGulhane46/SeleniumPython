#how to find how many input boxex present in web page 
#how to provide value into text box
#how to get the status

from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome(executable_path="C:/Users\Android - PC\Downloads\drivers\chromedriver.exe")
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

#find how many elements are there

inputboxes = driver.find_elements(By.CLASS_NAME,'text_field')
print(len(inputboxes))

status= driver.find_element(By.ID,'RESULT_TextField-1').is_displayed()
print("displayed or not",status) #true or false
#how to provide values into text box

driver.find_element(By.ID,'RESULT_TextField-1').send_keys('akshay')
driver.find_element(By.ID,'RESULT_TextField-2').send_keys('gulhane')
driver.find_element_by_id("RESULT_TextField-3").send_keys('123545698')
