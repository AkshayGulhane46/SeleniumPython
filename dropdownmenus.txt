from selenium import webdriver
from selenium.webdriver.support.select import Select

driver= webdriver.Chrome(executable_path = "C:/Users\Android - PC\Downloads\drivers\chromedriver.exe")
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

element= driver.find_element_by_id("RESULT_RadioButton-9")

drp=Select(element)

#select by visible text

#drp.select_by_visible_text('Morning')

#select by index

#drp.select_by_index(2)

#select by value
drp.select_by_value('Radio-2')

#capture number of all options in dropdown

print(len(drp.options))
all_options=drp.options

for option in all_options:
    print(option.text)
