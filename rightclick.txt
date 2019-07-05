from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path="C:/Users\Android - PC\Downloads\drivers\chromedriver.exe")

driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")

button = driver.find_element_by_xpath("/html/body/div/section/div/div/div/p/span")

actions= ActionChains(driver)

actions.context_click(button).perform()