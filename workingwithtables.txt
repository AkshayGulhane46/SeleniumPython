from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome(executable_path="C:/Users\Android - PC\Downloads\drivers\chromedriver.exe")

driver.get("file:///D:/appium/selenium%20with%20python/data/index.html")

rows=len(driver.find_elements_by_xpath("/html/body/table/tbody/tr"))

cols=len(driver.find_elements_by_xpath("/html/body/table/tbody/tr[1]/th"))

print(rows)
print(cols)
print("Products"+"Article"+"Price")
#for r in range(2,5)  #2,3,4 rows will returned
for r in range(2,rows+1):
    for c in range (1,cols+1):
        value = driver.find_element_by_xpath("/html/body/table/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(value,end=' ')
    print()
