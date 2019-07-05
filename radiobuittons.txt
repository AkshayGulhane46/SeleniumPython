#radio buttons selected or not
#click

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver =webdriver.Chrome(executable_path="C:/Users\Android - PC\Downloads\drivers\chromedriver.exe")
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

#working with radio buttons

status=driver.find_element_by_id("RESULT_RadioButton-7_0").is_selected()
print(status)


status=driver.find_element_by_id("RESULT_RadioButton-7_1").is_selected()
print(status)

#working with checkboxes

driver.find_element_by_id("RESULT_CheckBox-9_6").click()


status=driver.find_element_by_id("RESULT_CheckBox-9_6").is_selected()
print(status)