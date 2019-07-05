from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path="C:/Users\Android - PC\Downloads\drivers\chromedriver.exe")

driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

driver.maximize_window()

source_elemenmt= driver.find_element_by_xpath("//*[@id='box6']")

dest_element=driver.find_element_by_xpath("//*[@id='box106']")

actions=ActionChains(driver)

actions.drag_and_drop(source_elemenmt,dest_element).perform() #perform drag and drpo


